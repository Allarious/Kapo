
from django.urls import reverse

from apps.accounts.forms.forms import SignUpForm, UserForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'Home_page.html', {})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        # user.refresh_from_db()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/index.html', {})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def sign_up(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        form = SignUpForm(request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            username = request.POST['username']
            password = request.POST['password']
            user.set_password(user.password)
            user.is_customer = True
            user.save()
            customer = form.save(commit=False)
            customer.user = user
            customer.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accounts:customer_home'))

        else:
            # print(form)
            # print(user_form)
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = SignUpForm()
    print("how")
    return render(request, 'SignUp1.html',
                  {'user_form': user_form, 'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_customer:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accounts:customer_home'))
                if user.is_manager:
                    login(request, user)
                    return render(request, 'managerProfile.html', {})
                if user.is_employee:
                    login(request, user)
                    return render(request, 'employeeProfile.html', {})
            else:
                return render(request, 'Login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Login.html', {'error_message': 'Invalid login'})
    return render(request, 'Login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))
