# from django.shortcuts import get_object_or_404
# from apps.accounts.forms.forms import UpdateProfileForm
# from apps.accounts.models import Profile
# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.shortcuts import redirect, render
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from django.views import generic
# from django.views.generic import FormView, RedirectView
from apps.accounts.forms.forms import SignUpForm, UserForm
# from apps.accounts.tokens import account_activation_token
#
#
# class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
#     form_class = UpdateProfileForm
#     success_url = '/accounts/panel'
#     template_name = 'accounts/profile/update_profile.html'
#     model = Profile
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(User, pk=self.request.user.id)
#
#
#
#
# class SignupView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = '/accounts/email_sent'
#     template_name = 'accounts/profile/signup.html'
#
#     def get_form_class(self):
#         form = super().get_form_class()
#         form.request = self.request
#         return form
#
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect(to='/accounts/email_confirm')
#     else:
#         return redirect(to='/accounts/email_invalid')
#
#
# def email_confirm(request):
#     return render(request=request, template_name='email/email_confirm.html')
#
#
# def email_invalid(request):
#     return render(request=request, template_name='email/email_invalid.html')
#
#
# def email_sent(request):
#     return render(request=request, template_name='email/email_sent.html')
#
#
# class LoginView(FormView):
#     success_url = '/accounts/panel'
#     form_class = AuthenticationForm
#     template_name = 'accounts/profile/login.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         request.session.set_test_cookie()
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#
#         return super(LoginView, self).form_valid(form)
#
#
# class LogoutView(LoginRequiredMixin, RedirectView):
#     url = '/'
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
#
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # users = Users.objects.filter(auth_user= request.user)
#                 playlists = Playlist.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'playlists': playlists})
#             else:
#                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'music/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'music/login.html')

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

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
            user =authenticate(username=username, password=password)
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
    return render(request, 'SignUp.html',
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
                return render(request, 'index.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'index.html', {'error_message': 'Invalid login'})
    return render(request, 'index.html')