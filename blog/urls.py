from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign-up/', views.signup, name='signup'),
    path('log-in/', views.login, name='login'),
    path('<str:slug>/', views.blogposts, name='blogposts'),
    path('post/<str:slug>/', views.post, name='post'),
]