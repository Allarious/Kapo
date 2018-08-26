from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.core.models import Configuration
from apps.customer.forms.forms import *
from apps.customer.models import Customer
from apps.accounts.decorators import customer_required
from django.urls import reverse
from apps.transactions.models import *
from apps.accounts.models import *



@login_required
@customer_required
def index(request):
    return render(request, 'Customer_HomePage.html', {})


# TODO badan fieldash kamel beshan tebghe model

@login_required
@customer_required
def update_customer_profile(request):
    user = MyUser.objects.get(username=request.user.username)
    # customer = user.customer
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES)
        form = EditCustomerProfile(request.POST)

        if user_form.is_valid() and form.is_valid():
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:

                            if attr == 'password':

                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])
            customer = Customer.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(customer, attr, form.data[attr])
            user.save()
            customer.save()
            return HttpResponseRedirect(reverse('customer:customer profile'))

        else:
            print(user_form.errors, form.errors)
            return render(request, 'customer_update.html',
                          {'user_form': user_form, 'form': form})

    else:
        user_form = EditUser()
        form = EditCustomerProfile()

    return render(request, 'customer_update.html',
                  {'user_form': user_form, 'form': form})


@login_required
@customer_required
def customer_profile_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'Profile.html', {'customer': customer, })


@login_required
@customer_required
def customer_home_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    karmozds = Configuration.objects.exclude(key='dollar').exclude(key='euro')
    dollar_rate = Configuration.objects.get(key='dollar')
    euro_rate = Configuration.objects.get(key='euro')
    return render(request, 'customer_home.html',
                  {'customer': customer, 'karmozds': karmozds, 'euro_rate': euro_rate, 'dollar_rate': dollar_rate})

def customer_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    notifications = Notification.objects.all().filter(owner=customer.user)
    print(notifications[0].seen)
    print(notifications[1].seen)
    notification = []
    for i in range(notifications.count()):
        notification.append(notifications[notifications.count() - 1 - i])
    Notification.objects.all().filter(owner=customer.user).update(seen=True)
    return render(request, 'customer_dashboard1.html', {'notifications': notification})

def message_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    messages = Message.objects.all().filter(receiver=customer.user)
    message = []
    for i in range(messages.count()):
        message.append(messages[messages.count() - 1 - i])
    return render(request, 'customer_message_dashboard.html', {'messages': message})