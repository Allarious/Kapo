from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.accounts.models import MyUser
from apps.manager.models import Manager
from apps.accounts.decorators import manager_required
from apps.customer.forms.forms import EditUser
from apps.manager.forms import EditManagerProfile
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
@login_required
@manager_required
def manager_profile_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    return render(request, 'manager_profile.html', {'manager': manager, })

@login_required
@manager_required
def index(request):
    return render(request, 'manager_HomePage.html', {})


@login_required
@manager_required
def update_manager_profile(request):
    user = MyUser.objects.get(username=request.user.username)
    # customer = user.customer
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES)
        form = EditManagerProfile(request.POST)

        if user_form.is_valid() and form.is_valid():
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:

                            if attr == 'password':

                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])
            manager = Manager.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(manager, attr, form.data[attr])
            user.save()
            manager.save()
            return HttpResponseRedirect(reverse('manager:manger_profile'))

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = EditUser()
        form = EditManagerProfile()

    return render(request, 'manager_edit.html',
                  {'user_form': user_form, 'form': form})