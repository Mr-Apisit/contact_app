from django.urls import path
from django.contrib.auth import views as auth_views
from officer import views



urlpatterns = [

    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="sign_up"),
    # path('details/', views.details, name='details'),
    path('login/', views.signIn_request, name="sign_in"),
    path("logout/", views.logout_request, name= "sign_out"),
    path('zone/', views.zone, name= "zone"),
    path('people/', views.member, name="member"),
    path('member/', views.blog_member, name="blog_member"),
    # path('add_member/', views.insert_member, name="insert_member"),
    path('home/กบสซ.', views.member_by_department_SUPPORT, name='บูรณาการ'),
    path('home/กมซ.', views.member_by_department_STANDARD, name='มาตรฐาน'),
    path('home/กวซ.', views.member_by_department_ENGINEER, name='วิศวกรรม'),
    path('home/สบช.', views.member_by_department_COMMAND, name='สั่งการ'),
    
# path('member')


]

