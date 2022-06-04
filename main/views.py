from django.shortcuts import redirect, render
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Profile, Group
from django.utils.dateparse import parse_date
import random
# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'main/index.html', context )


@login_required(login_url='/login/')
def profile(request):
    context = {
        'profile':Profile.objects.get(user=User.objects.get(username=request.user.username))
    }
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        city = request.POST.get("city")

        user = User.objects.get(username=request.user.username)
        user.first_name = first_name
        user.last_name = last_name

        profile = Profile.objects.get(user=user)
        profile.age = int(age)
        profile.city = city
        user.save()
        profile.save()
        return redirect('profile')
    else:
        return render(request, 'main/profile.html', context)

@login_required(login_url='/login/')
def leave_from_group(request, id):
    group = Group.objects.get(id=id)
    group.users.remove(request.user)
    group.save()
    return redirect("groups")

@login_required(login_url='/login/')
def add_to_group(request, id):
    group = Group.objects.get(id=id)
    group.users.add(request.user)
    group.save()
    return redirect("groups")

@login_required(login_url='/login/')
def users(request):
    context = {
        'users':User.objects.all(),
        'profiles':Profile.objects.all(),
        'groups':Group.objects.all()
    }

    return render(request, 'main/users.html', context)

def change_group(request):
    username = request.POST.get("username")
    group_id = int(request.POST.get("group"))
    print(group_id)
    user = User.objects.get(username=username)
    if group_id != -1:
        group = Group.objects.get(id=group_id)
        if user not in group.users.all():
            group.users.add(user)
            group.save()
    elif group_id == -1:
        for group in Group.objects.all():
            if user in group.users.all():
                group.users.remove(user)
                group.save()
    else:
        print("alredy")
    return redirect("users")


def fix_groups_participants(groups):
    for group in groups:
        group.filled = len(group.users.all())
        group.save()
        group.id

@login_required(login_url='/login/')
def groups(request):
    fix_groups_participants(Group.objects.all())
    context = {
        'groups':Group.objects.all()
    }
    return render(request, 'main/groups.html', context)

class MyLoginView(LoginView):
    template_name = "main/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class RegisterUserView(CreateView):
    model = User
    template_name = "main/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = "Пользователь успешно создан"

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        patronym = request.POST.get("patronym")
        IIN = request.POST.get("IIN")
        dateofbirth = request.POST.get("dateofbirth")
        password = request.POST.get('password')
        user = User(username=username,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        print(request.POST)
        dateofbirth = parse_date(dateofbirth)
        print(dateofbirth)
        profile = Profile(user=user, dateofbirth=dateofbirth, IIN=IIN,patronym=patronym)
        profile.save()
        
        return redirect("login")
    else:
        return render(request, 'main/register.html')