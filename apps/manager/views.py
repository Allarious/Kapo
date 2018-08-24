from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.manager.models import Manager
from apps.accounts.decorators import manager_required



# Create your views here.
@login_required
@manager_required
def manager_profile_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    return render(request, 'manager-profile.html', {'manager': manager, })

@login_required
@manager_required
def index(request):
    return render(request, 'manager_HomePage.html', {})