from django.urls import path
from django.contrib.auth import views as auth_views
from officer import views



urlpatterns = [

    path('', views.index, name="index"),
    path('zone/', views.zone, name="zone"),
    path('register/', views.register, name="sign_up"),
    # path('details/', views.details, name='details'),
    path('login/', views.signIn_request, name="sign_in"),
    path("logout/", views.logout_request, name= "sign_out"),
    path('member/', views.member, name="member"),
    path('zone3/', views.member_by_department_IMC, name='IMC'),



# path('member')


]
