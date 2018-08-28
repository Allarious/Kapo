from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.accounts.models import Notification, Message
from apps.core.models import Configuration
from apps.manager.models import Manager
from apps.transactions.models import *


def index(request):
    if request.user.is_authenticated and request.user.is_customer:
        return HttpResponseRedirect(reverse('customer:index'))
    elif request.user.is_authenticated and request.user.is_employee:
        return HttpResponseRedirect(reverse('employee:index'))
    elif request.user.is_authenticated and request.user.is_manager:
        return HttpResponseRedirect(reverse('manager:index'))
    return render(request, 'Home_page.html', {})


def contact_us_view(request):
    if (request.POST):
        notification = Notification()
        message = Message()
        message_receiver = get_object_or_404(MyUser, id=Manager.objects.all()[0].user.id)
        # message_receiver = MyUser.objects.get(username=receiver)
        message.receiver = message_receiver
        notification.owner = message_receiver
        notification.type = 'message'
        user = MyUser()
        print(user.id)
        id = MyUser.objects.all().count()
        user.username = "user" + str(id )
        user.set_password("1234")
        user.email = "user" + str(user.id) +"@gmail.com"
        user.save()
        message.sender = user
        message.subject = request.POST.get("subject")
        message.message = request.POST.get('message')
        notification.save()
        message.save()
    return render(request, 'contact-us.html', {})


def about_us_view(request):
    return render(request, 'info.html', {})


def policy_view(request):
    return render(request, 'policy.html', {})


def wages_list_view(request):
    wages = Configuration.objects.all().exclude(key__in=['dollar', 'euro'])
    for wage in wages:
        tmp = '0' + wage.value[1:]
        # tmp = '0'
        print(tmp)
        wage.value = tmp
    rates = Configuration.objects.all().filter(key__in=['dollar', 'euro'])
    return render(request, 'wages.html', {'rates': rates, 'wages': wages})


def transition_test_view(request):
    rates = Configuration.objects.all().filter(key__in=['dollar', 'euro'])
    for rate in rates:
        if rate.key == 'dollar':
            dollar = float(rates[1].value)
        if rate.key == 'euro':
            euro = float(rates[0].value)
    return render(request, 'trans.html', {'dollar': dollar, 'euro':euro})
