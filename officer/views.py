from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from officer.forms import NewUserForm, UserForm, ProfileForm
from django.contrib import messages
from .models import Destination
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
import django_filters.rest_framework as backends
from officer.models import Department

#******************* 👍 Operations TARGET user  *************************#


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("signIn_request")
    form = NewUserForm
    return render(request=request, template_name="auth/sign_up.html", context={"register_form": form})


# def signUp_request(request):
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             user.refresh_from_db()
#             user.profile.username = form.cleaned_data.get('username')
#             user.profile.email = form.cleaned_data.get('email')
#             user.profile.title = form.cleaned_data.get('title')
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             user.profile.nickname = form.cleaned_data.get('nickname')
#             user.profile.phone = form.cleaned_data.get('phone')
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             messages.success(
#                 request, f'บัญชีถูกสร้างแล้วนะ {username}ด้วย email : {email} !')
#             return redirect('signIn_request')
#         messages.error(
#             request, "Unsuccessful ไม่สำเร็จ. Invalid information.")
#     form = UserRegister()
#     return render(request, 'auth/sign_up.html', {'signUp_request_form': form})


# def details(request):
#     if request.method == 'POST':
#         form = Detail(request.POST)
#         if form.is_valid():
#             user.refresh_from_db()
#             user.profile.title = form.cleaned_data.get('title')
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             # user.profile.nickname = form.cleaned_data.get('nickname')
#             user.profile.phone = form.cleaned_data.get('phone')
#             # user.profile.birth_date = form.cleaned_data.get('birth_date')
#             # user.profile.profile_picture = form.cleaned_data.get('profile_picture')
#             user.save()
#             first_name = user.first_name
#             phone = user.phone
#             messages.success(
#                 request, f'สร้างโปรไฟล์เรียบร้อยด้วยชื่อ {first_name} เบอร์โทร : {phone} !')
#             return redirect('zone')
#         messages.error(
#             request, "Unsuccessful registration. Invalid information.")
#     form = Detail()
#     return render(request, 'auth/sign_up.html', {'details': form})


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


# @login_required

# def member(request):
#     user_form = UserForm(instance=request.user)
#     profile_form = ProfileForm(instance=request.user.profile)
#     return render(request=request, template_name="member/list_member.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })


# @login_required
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})


@login_required
def zone(request):
    department = Department.objects.all()
    return render(request=request, template_name="member/home.html", context={'department': department})


# def user(request):
#     if request.method == 'POST':
#         user_form = userForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid():
# 		user_form.save()
# 		    messages.success(request, ('Your profile was successfully updated!'))
# 		elif profile_form.is_valid():
# 		    profile_form.save()
# 		    messages.success(request,('Your wishlist was successfully updated!'))
# 		else:
# 		    messages.error(request,('Unable to complete request'))
# 		return redirect ("user:user")

# 	user_form = UserForm(instance=request.user)
# 	profile_form = ProfileForm(instance=request.user.profile)


#     return render(request = request,template_name = 'user/profile.html', context={"user":request.user,
# 		"user_form": user_form, "profile_form": profile_form })


# def list_user(request):
#     if request.method == "POST":
# 		position_id = request.POST.get("position_pk")
# 		position = Product.objects.get(id = product_id)
# 		request.user.profile.position.add(product)
# 		messages.success(request,(f'{product} added to wishlist.'))
# 		return redirect ('user:list_user')
# 	position = Product.objects.all()
# 	paginator = Paginator(position, 18)
# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	return render(request = request, template_name="list_user.html", context = { "page_obj":page_obj})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')
