from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User

from blog.models import Categorie, Contact, Post, Comment

# Home HTMl
def home(request):
    allCategory = Categorie.objects.all() # Getting all the objects of Categorie class
    nowPosts = Post.objects.order_by('-created_on') # Getting the recently created posts

    context = {'allCategory':allCategory, 'nowPosts':nowPosts}
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    # Performing the Post request for giving the information of the user
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

    # Checking the filled fields are according to given requirements or not  
        if len(name) < 2 or len(email) < 3 or len(content) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(name=name, email=email, reason=content)
            contact.save()
            messages.success(request, 'Your response has been successfully submitted.')

    return render(request, 'home/contact.html')


# Authentication APIs

def search(request):
    # Query, where all the search term will be given
    query = request.GET['query']

    # Giving error if searched more than 78 keywords
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPosts = allPostsTitle|allPostsContent # Merging the title and post in a variable so that both can be given for results during search
    if allPosts.count() == 0:
        messages.warning(request, 'No search results found. Please refine your query.')

    context = {"allPosts":allPosts, "query":query}
    return render(request, 'home/search.html', context)

def signup(request):
    # Performing the Post request for signing up
    if request.method == 'POST':
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']

    # Some Restrictions for the user input
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters.")
        if username.isalnum():
            messages.error(request, "Username must contain alphabets and numbers. Sign Up Again")
            return redirect('home')

        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        messages.success(request, "Your blog account has been created Successfully!")
        return redirect('home')
    return render(request, 'home/sign-up.html')

def login(request):
    # Performing the Post request for logging in
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']

    # Authenticating
        user = authenticate(request, username=username, password=password)

    # If not exist
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!")

    return render(request, 'home/log-in.html')

def logout(request):
    # Logging out
    auth_logout(request)
    messages.success(request, "Succesfully Logged In!")
    return redirect('home')


# Blog HTML
def blogposts(request, slug):
    # Getting the catgeories by slug
    try:
        allCat = Categorie.objects.get(slug=slug)
    except Categorie.DoesNotExist:
        allCat = None
    # Getting the blog post by slug of category defined above
    post_list = Post.objects.filter(post_category = allCat)

    # Intializing the paginator for pagination of blog posts
    paginator = Paginator(post_list, 5)
    # GET request returns the current page number
    page_number = request.GET.get('page')
    # Getting the page and storing it in page_obj
    page_obj = paginator.get_page(page_number)
    
    context = {'allCat':allCat, 'page_obj':page_obj} 
    return render(request, 'blogs/Blogposts.html', context)

def post(request, slug):

    post_list = Post.objects.filter(slug=slug).first() # for slug
    comments = Comment.objects.filter(post = post_list, parent=None) # for comment on particular post with no parent
    replies = Comment.objects.filter(post = post_list).exclude(parent=None) # for comment on particular post with parent

    replyDict = {}
    for reply in replies:
        # If the serial no. of reply is not present in the dictionary then give it a list of reply
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post_list' : post_list, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'blogs/post.html', context)

def postcomment(request):
    # Performing Post request to get the comments of the users
    if request.method == "POST":
        comment = request.POST.get('commenttext')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        # If the parent is empty
        if parentSno == "":
            comment = Comment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, 'Your Comment has been successfully added.')
        else:
            parent = Comment.objects.get(sno=parentSno)
            comment = Comment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, 'Your Reply has been successfully added.')

    return redirect(f'/post/{post.slug}')


# Forget Password

def password_reset(request):
    email = "bro@gmail.com"
    userEmail = User.objects.filter(email=email)
    if userEmail.exists():
        print("Yes the user exists")
    else:
        print("No")
    return HttpResponse("Reset your password")

def password_reset_done(request):
    return HttpResponse("We've sent you an email to your email if valid")

def password_reset_confirm(request):
    return HttpResponse("Write your new password here")

def password_reset_complete(request):
    return HttpResponse("Your password has been changed")