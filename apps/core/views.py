from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.core.models import Configuration
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
    return render(request, 'contact_us.html', {})


def about_us_view(request):
    return render(request, 'info.html', {})


def policy_view(request):
    return render(request, 'policy.html', {})


def wages_list_view(request):
    wages = Configuration.objects.all().exclude(key__in=['dollar', 'euro'])
    rates = Configuration.objects.all().filter(key__in=['dollar', 'euro'])
    return render(request, 'wages.html', {'rates': rates, 'wages': wages})


def transition_test_view(request):
    rates = Configuration.objects.all().filter(key__in=['dollar', 'euro'])
    return render(request, 'trans.html', {'rates': rates})
