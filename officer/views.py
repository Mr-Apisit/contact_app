from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from officer.decorators import unauthenticated_user
from django.core.paginator import Paginator
# Create your views here.
from django.conf import settings
from officer.models import Department, Member, Tag
from officer.forms import NewUserForm, MyAuthForm, UserForm, ProfileForm, MemberForm
from django.contrib import messages
\
    
#******************* 👍 SIGN UP  *************************#
@csrf_exempt
@unauthenticated_user
def register(request):
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            # group = Group.objects.get(name='member')  
            # user.groups.add(group)     
            # Member.objects.create(
            #     user=user,
            #     phone = user.phone,              
            #     )           
            messages.success(request, f"ลงทะเบียนใช้งานสำเร็จแล้วด้วยเบอร์ : {username}")
            return redirect("sign_in")
        messages.error(
            request, "ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")

    return render(request=request, template_name="auth/sign_up.html", context={"form": form})

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
                messages.info(request, f"เข้าใช้งานด้วย {username}.")
                return redirect('home')
            else:
                messages.error(request, " username or password อาจไม่ถูกต้อง")
        else:
            messages.error(request, "username or password อาจไม่ถูกต้อง")
    form = MyAuthForm()
    return render(request=request, template_name="auth/sign_in.html", context={"signIn_request_form": form})


#******************* 👍 EXAM  *************************#

def home(request):
    department = Department.objects.all()[:6]
    develop = Member.objects.filter(skill_tag__tag_slug='developer')[:3]
    database = Member.objects.filter(skill_tag__tag_slug='database')[:3]
    design = Member.objects.filter(skill_tag__tag_slug='designer')[:3]
    server = Member.objects.filter(skill_tag__tag_slug='server')[:3]

    return render(request, "member/home.html", {
        'develop': develop,
        'database' : database,
        'design' : design,
        'server' : server,
        'department': department,
        })



#******************* 👍 MEMBER  *************************#
        

        
@login_required(login_url='sign_in')
def blog_member(request, skill_tag):
    if skill_tag == 'search_member':
        tag = ''
        member = Member.objects.all().order_by('-created_at')

    else: 
        tag = Tag.objects.get(tag_slug=skill_tag)
        member = Member.objects.filter(skill_tag=tag).order_by("-created_at")    
    paginator = Paginator(member, 4)
    page_number = request.GET.get('page')
    member_obj = paginator.get_page(page_number)

    return render(request, "member/search_member.html", context={'member': member_obj, 'tag': tag})

@login_required(login_url='sign_in')
def detail_member(request, phone):
    member = Member.objects.get(phone=phone)
    return render(request, 'member/detail.html', {'member': member})


#******************* 👍  QUERY DEPARTMENT *************************#


@login_required(login_url='sign_in')
def zone(request):
    department = Department.objects.all()
    return render(request=request, template_name="member/zone.html", context={'department': department})


@login_required(login_url='sign_in')
def list_member_by_location(request,short_name):
    if short_name == 'zone':
        department = Department.objects.all()
    elif short_name == 'กบสซ.':
        member = Member.objects.filter(location__short_name="กบสซ.")
    elif short_name == 'กวซ.':
        member = Member.objects.filter(location__short_name="กวซ.")
    elif short_name == 'กมซ.':
        member = Member.objects.filter(location__short_name="กมซ.")
    elif short_name == 'สบช.':
        member = Member.objects.filter(location__short_name="สบช.")

    paginator = Paginator(member, 4)
    page_number = request.GET.get('page')
    member_obj = paginator.get_page(page_number)
    
    return render(request, "member/search_zone.html", context={'member': member_obj, 'member': member, 'short_name': short_name})


#******************* 👍 QUERY MEMBER BY DEPARTMENT  *************************#


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

#******************* 👍 User  CRUD *************************#

@login_required(login_url='sign_in')
def userpage(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        member_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile.members)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your Profile was selected!'))
        elif member_form.is_valid():
            member_form.save()
            messages.success(request,('Your Profile was successfully updated!'))

        else:
            messages.error(request,('Unable to complete request'))
        return redirect ("userpage")
    # member = Member.objects.all()
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    member_form = ProfileForm(instance=request.user.profile.members)
    return render(request=request, template_name="member/user.html", 
                  context={
                            "user": request.user,
                            "user_form": user_form,
                            "profile_form": profile_form,
                            "member_form": member_form
                 })


@login_required(login_url='sign_in')
def profile_create(request):
    
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            add_member = form.save(commit=False)
            add_member.user = request.user
            add_member.save()
            title = form.cleaned_data.get('title')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            nick_name = form.cleaned_data.get('nick_name')
            phone = form.cleaned_data.get('phone')
            profile_picture = form.cleaned_data.get('profile_picture')
            position = form.cleaned_data.get('position')
            location = form.cleaned_data.get('location')
            skill_tag = form.cleaned_data.get('skill_tag')
            about_me = form.cleaned_data.get('about_me')         

            messages.success(request, f"เพิ่มโปรไฟล์ใช้งานสำเร็จแล้วนะคุณ {nick_name}")
            return redirect ("blog_member")
        else:          
            messages.error( request, "ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")
    form = MemberForm
    return render(request, "member/add_member.html", {"form": form})

@login_required(login_url='sign_in')
def update_profile(request, phone):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance = request.user.profile.members)
        if form.is_valid():
            add_member = form.save(commit=False)
            add_member.user = request.user
            form.save()
            title = form.cleaned_data.get('title')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            nick_name = form.cleaned_data.get('nick_name')
            phone = form.cleaned_data.get('phone')
            profile_picture = form.cleaned_data.get('profile_picture')
            position = form.cleaned_data.get('position')
            location = form.cleaned_data.get('location')
            skill_tag = form.cleaned_data.get('skill_tag')
            about_me = form.cleaned_data.get('about_me')  
            
            messages.success(request, "บันทึกแล้ว")
            return redirect("userpage")
    form = MemberForm(instance=request.user.profile.members)
    return render(request, 'member/update_member.html', context={"form":form})


@login_required(login_url='sign_in')
def delete_profile(request, phone):
    member = Member.objects.get(phone=phone)
    if member.phone != request.user.phone:
        messages.error(request,'Error')
        redirect("/member/detail/")
    member.delete()
    messages.success(request, 'delete success')
    logger.info('Delete member Success')
    return redirect('member')


#******************* 👍 SIGN OUT  *************************#

@csrf_exempt
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')
