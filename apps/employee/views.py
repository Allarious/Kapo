
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.employee.models import Employee
from apps.accounts.decorators import employee_required



# Create your views here.
@login_required
@employee_required
def employee_profile_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    return render(request, 'employee-profile.html', {'employee': employee, })

@login_required
@employee_required
def index(request):
    return render(request, 'employee_HomePage.html', {})