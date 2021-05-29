from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from officer.decorators import unauthenticated_user
from django.core.paginator import Paginator
# Create your views here.
from django.conf import settings
from officer.models import Department, Member, Tag
from officer.forms import NewUserForm, MyAuthForm, UserForm, ProfileForm
from django.contrib import messages
\
    
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
        messages.error(
            request, "ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")
    form = NewUserForm
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
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = MyAuthForm()
    return render(request=request, template_name="auth/sign_in.html", context={"signIn_request_form": form})


#******************* 👍 EXAM  *************************#

def home(request):
    department = Department.objects.all()[:6]
    dev = Member.objects.filter(skill_tag__tag_name='นักพัฒนา')[:3]
    db = Member.objects.filter(skill_tag__tag_name='ฐานข้อมูล')[:3]
    design = Member.objects.filter(skill_tag__tag_name='นักออกแบบ')[:3]

    return render(request, "member/home.html", {
        'dev': dev,
        'db' : db,
        'design' : design,
        'department': department
        })



#******************* 👍  QUERY DEPARTMENT *************************#


@login_required(login_url='sign_in')
def zone(request):
    department = Department.objects.all()
    return render(request=request, template_name="member/zone.html", context={'department': department})

#******************* 👍 MEMBER  *************************#

def blog(request):
	blog = Article.objects.all().order_by('-article_published')
	paginator = Paginator(blog, 25)
	page_number = request.GET.get('page')
	blog_obj = paginator.get_page(page_number)
	return render(request=request, template_name="member/blog.html", context={"blog":blog_obj})


@login_required(login_url='sign_in')
def blog_member(request, skill_tag):
    if skill_tag == 'search_member':
        tag = ''
        member = Member.objects.all().order_by('-position')
    else:
        tag = Tag.objects.get(tag_slug=skill_tag)
        member = Member.objects.filter(skill_tag=tag).order_by("-position")    
    paginator = Paginator(member, 25)
    page_number = request.GET.get('page')
    member_obj = paginator.get_page(page_number)

    return render(request, "member/search_member.html", context={'member': member_obj, 'tag': tag})

@login_required(login_url='sign_in')
def detail_member(request, phone):
    member = Member.objects.get(phone=phone)
    return render(request, 'member/detail.html', {'member': member})

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

#******************* 👍 CREATE EDIT DELETE  *************************#

@login_required(login_url='sign_in')
def userpage(request):
    user_form = UserForm(instance=request.user)
    member = Member.objects.all()
    return render(request=request, template_name="member/user.html", context={"user": request.user, "user_form": user_form, "member": member})


@csrf_exempt
@login_required(login_url='sign_in')
def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            member.save()          
            messages.success(request, "ลงทะเบียนใช้งานสำเร็จแล้ว")
            return redirect("member")        
        messages.error( request, "ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")   
    member = ProfileForm        
    return render(request, "member/add_profile.html", {"form": member})

@csrf_exempt
@login_required(login_url='sign_in')
def update_profile(request, phone):
    member = Member.objects.get(pk=phone)
    if member.phone != request.user.phone:
        message.error(request,"ไม่สามารถลงทะเบียนได้เนื่องจากข้อมูลไม่ตรงเงื่อนไข")
        return redirect('member')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = member)
        if form.is_valid():
            form.save()
            logger.info('อัปเดตโปรไฟล์เรียบร้อย')
            messages.success(request, "บันทึกแล้ว")
            return render(request, 'member/update_profile.html', context)


@csrf_exempt
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
    return redirect('zone')
