from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('postcomment/', views.postcomment, name='postcomment'),
    path('postreply/', views.postreply, name='postreply'),
    path('', views.home, name='home'),
    path('aboutme/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:slug>/', views.blogposts, name='blogposts'),
    path('post/<str:slug>/', views.post, name='post'),
]