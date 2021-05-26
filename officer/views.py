from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from officer.decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.

from officer.models import Department, Member
from officer.forms import NewUserForm, UserForm, ProfileForm
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
            messages.success(request, "Registration successful." )
            return redirect("zone")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "auth/sign_up.html", {"register_form": form})


#******************* 👍 SIGN IN *************************#

@csrf_exempt
@unauthenticated_user
def signIn_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('zone')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="auth/sign_in.html", context={"signIn_request_form": form})


#******************* 👍 EXAM  *************************#

@login_required(login_url='sign_in')
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})


#******************* 👍  *************************#

def zone(request):
    department = Department.objects.all()
    return render(request=request, template_name="member/home.html", context={'department': department})

#******************* 👍 MEMBER  *************************#

def insert_member(request):
    
    return render(request, "member/includes/add_member.html", context={'insert_member':insert_member})


@login_required(login_url='sign_in')
def member(request):
    member = Member.objects.all()
    return render(request, "member/list_member.html",context={'member':member})

@login_required(login_url='sign_in')
def member_by_department_IMC(request):
    department = Department.objects.all()
    member = Member.objects.filter(location__name="กองวิศวกรรมซอฟต์แวร์")
    # department_id = Department.objects.get(name=pk)
    
    return render(request, 'member/zone3/list_member.html', {'member':member, 'department':department})
    
    
    

#******************* 👍 SIGN OUT  *************************#

@csrf_exempt
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('zone')


