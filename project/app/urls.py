from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
  path('',views.index,name='index'),
  path('contact',views.contact,name='contact'),
  path('about',views.about,name='about'),
  path('handleBlog',views.handleBlog,name='handleBlog'),
  path('services',views.services,name='services'),
  path('signUp',views.signUp,name='signUp'),
  path('login',views.handlelogin,name='handlelogin'),
  path('logout',views.handlelogout,name='handlelogout'),


]
