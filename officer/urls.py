from django.urls import path
from django.contrib.auth import views as auth_views
from officer import views



urlpatterns = [

    path('', views.home, name="home"),
    path('register/', views.register, name="sign_up"),
    # path('details/', views.details, name='details'),
    path('login/', views.signIn_request, name="sign_in"),
    path("logout/", views.logout_request, name= "sign_out"),
    path("user", views.userpage, name = "userpage"),
    path('zone/', views.zone, name= "zone"),
    path('<skill_tag>/', views.blog_member, name="member"),
    path('search_member/', views.blog_member, name="blog_member"),
    path('member/<phone>', views.detail_member, name="detail"),
    path('member/delete/<phone>', views.delete_profile, name="delete_member"),
    path('member/update/<phone>', views.update_profile, name="update_member"),
    path('member/create/', views.profile_create, name="add_member"),
    # path('home/<short_name>', views.list_member_by_location, name="list_by_locate"),
    path('zone/กบสซ.', views.member_by_department_SUPPORT, name='บูรณาการ'),
    path('zone/กมซ.', views.member_by_department_STANDARD, name='มาตรฐาน'),
    path('zone/กวซ.', views.member_by_department_ENGINEER, name='วิศวกรรม'),
    path('zone/สบช.', views.member_by_department_COMMAND, name='สั่งการ'),
    
# path('member')


]

