from re import template
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

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
    
    # Forget Password
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
    
    # Blog
    path('<str:slug>/', views.blogposts, name='blogposts'),
    path('post/<str:slug>/', views.post, name='post'),
    
]