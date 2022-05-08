from re import template
from django.urls import path
from blog import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Comments
    path('postcomment/', views.postcomment, name='postcomment'),

    # Nav Links
    path('aboutme/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    
    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'), 
    
    # Blog
    path('<str:slug>/', views.blogposts, name='blogposts'),
    path('post/<str:slug>/', views.post, name='post'),
    
]