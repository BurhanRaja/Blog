from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages

from blog.models import Categorie, Contact, Post

# Create your views here.
def home(request):
    # Gtting all the objects of Categorie class
    allCategory = Categorie.objects.all()
    # Getting the recently created posts
    nowPosts = Post.objects.order_by('-created_on')

    context = {'allCategory':allCategory, 'nowPosts':nowPosts}
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(content) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(name=name, email=email, reason=content)
            contact.save()
            messages.success(request, 'Your response has been successfully submitted.')

    return render(request, 'home/contact.html')

def search(request):
    return render(request, 'home/search.html')

def signup(request):
    return render(request, 'home/sign-up.html')

def login(request):
    return render(request, 'home/log-in.html')

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
    
    
    context = {'allCat':allCat, 'posts':post_list, 'page_obj':page_obj} 
    return render(request, 'blogs/Blogposts.html', context)

def post(request, slug):

    post_list = Post.objects.filter(slug=slug).first()

    context = {'post_list' : post_list}
    return render(request, 'blogs/post.html', context)
