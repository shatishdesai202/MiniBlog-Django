from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm, PostForm, ContactForm
from .models import Post, Contact
from django.contrib import messages


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'message send Sucessfully')
            form = ContactForm()
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def dashboard(request):
    user = request.user
    if request.user.is_authenticated:
        if request.user.is_superuser:
            user_post = Post.objects.all()
            full_name = user.get_full_name()
            grp = user.groups.all()
        else:
            user_post = Post.objects.filter(post_by=user)
            full_name = user.get_full_name()
            grp = user.groups.all()
        context = {'user_post': user_post, 'fullname': full_name, 'grp': grp}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponseRedirect('/login/')


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            form = SignupForm()
            messages.success(request, 'Signup sucessfully')
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login Sucessful')
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'Login failed')
                return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    messages.info(request, 'logout')
    return HttpResponseRedirect('/login/')


def add_post(request):
    if request.method == "POST":
        form = Post()
        user = request.user
        names = request.POST['name']
        desc = request.POST['desc']

        form = Post(name=names, desc=desc, post_by=user)
        form.save()
        messages.success(request, 'Post Added Sucessfully')
        return HttpResponseRedirect('/dashboard/')
    else:

        form = Post()
    context = {'form': form}
    return render(request, 'addpost.html', context)


def delete_post(request, id):
    form = Post.objects.get(pk=id)
    form.delete()
    messages.success(request, 'delete post Sucessfully')
    return HttpResponseRedirect('/dashboard/')


def update_post(request, id):
    posts = Post.objects.get(pk=id)
    if request.method == "POST":
        print('post Enter')
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post Updated')
            return HttpResponseRedirect('/dashboard/')
    else:
        print('get request')
        form = PostForm(instance=posts)
    context = {'form': form}
    return render(request, 'updatepost.html', context)


def postdetail(request, id):
    post = Post.objects.get(pk=id)

    context = {'post': post}
    return render(request, 'postdetail.html', context)
