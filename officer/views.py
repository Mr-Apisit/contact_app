from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from officer.decorators import unauthenticated_user
from django.core.paginator import Paginator
# Create your views here.

from officer.models import Department, Member
from officer.forms import NewUserForm, MyAuthForm, UserForm, ProfileForm
from django.contrib import messages
from .models import Destination


#******************* 👍 SIGN UP  *************************#
@csrf_exempt
@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ลงทะเบียนใช้งานสำเร็จแล้ว")
            return redirect("home")
        messages.error(request, "ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")
    form = NewUserForm
    return render(request = request,template_name="auth/sign_up.html", context = {"form": form})

#******************* 👍 SIGN IN *************************#

@csrf_exempt
@unauthenticated_user
def signIn_request(request):
    if request.method == "POST":
        form = MyAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = MyAuthForm()
    return render(request=request, template_name="auth/sign_in.html", context={"signIn_request_form": form})


#******************* 👍 EXAM  *************************#

@login_required(login_url='sign_in')
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def home(request):
    department = Department.objects.all()
    member = Member.objects.all().order_by('-position')
    paginator = Paginator(member, 25)
    page_number = request.GET.get('page')
    insert_member_obj = paginator.get_page(page_number) 
    return render(request, "member/home.html", {'member':insert_member_obj , 'department':department })

#******************* 👍  QUERY DEPARTMENT *************************#

@login_required(login_url='sign_in')
def zone(request):
    department = Department.objects.all()
    return render(request=request, template_name="member/zone.html", context={'department': department})

#******************* 👍 QUERY MEMBER  *************************#

@login_required(login_url='sign_in')
def member(request):
    member = Member.objects.all()
    return render(request, "member/member.html", {'member': member})

    

#******************* 👍 MEMBER  *************************#

@login_required(login_url='sign_in')
def blog_member(request):
    
    member = Member.objects.all().order_by('-position')
    paginator = Paginator(member, 25)
    page_number = request.GET.get('page')
    insert_member_obj = paginator.get_page(page_number)    

    return render(request, "member/search_member.html", context={'insert_member': insert_member_obj})

def detail_member(request, member_phone):
    member = Member.objects.get(phone=member_phone)
    return render(request,'member/detail.html', {'member':member})

#******************* 👍 QUERY MEMBER BY DEPARTMENT  *************************#

# @login_required(login_url='sign_in')
# def list_member_by_location(request, short_name):
#     department = Department.objects.all()
#     member = Member.objects.get(location__short_name=short_name)
#     return render(request, 'member/member.html', {'member':member})

@login_required(login_url='sign_in')
def member_by_department_ENGINEER(request):
    department = Department.objects.all()
    member = Member.objects.filter(location__short_name="กวซ.")    
    
    return render(request, 'member/zone3/list_member.html', {'member': member, 'department': department})

@login_required(login_url='sign_in')
def member_by_department_SUPPORT(request):
    
    department = Department.objects.all()
    member = Member.objects.filter(location__short_name="กบสซ.")    
    
    return render(request, 'member/zone1/list_member.html', {'member': member, 'department': department})

@login_required(login_url='sign_in')
def member_by_department_STANDARD(request):
    department = Department.objects.all()
    member = Member.objects.filter(location__short_name="กมซ.")    
    
    return render(request, 'member/zone2/list_member.html', {'member': member, 'department': department})

@login_required(login_url='sign_in')
def member_by_department_COMMAND(request):
    department = Department.objects.all()
    member = Member.objects.filter(location__short_name="สบช.")    
    
    return render(request, 'member/zone4/list_member.html', {'member': member, 'department': department})


#******************* 👍 SIGN OUT  *************************#

@csrf_exempt
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('zone')
