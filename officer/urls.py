from django.urls import path
from django.contrib.auth import views as auth_views
from officer import views
from officer import forms

urlpatterns = [

    path('', views.index, name="index"),
    path('zone/', views.zone, name="zone"),
    path('register/', views.register, name="register"),
    # path('details/', views.details, name='details'),
    path('login/', views.signIn_request, name="signIn_request"),
    path('logout/', auth_views.LoginView.as_view(), name='logout_request'),
    # path('member/', views.member, name="member")


    # path('member')


]
