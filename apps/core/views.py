from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    return render(request, 'about_us.html', {})


def policy_view(request):
    return render(request, 'policy.html', {})


