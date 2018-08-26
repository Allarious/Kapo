from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.accounts.models import MyUser
from apps.customer.models import Customer
from apps.manager.models import Manager
from apps.accounts.decorators import manager_required
from apps.customer.forms.forms import EditUser
from apps.manager.forms.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.transactions.functions import *


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


@login_required
@manager_required
def manager_check_transaction_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    if request.method == 'POST':
        if request.POST.get('checked transaction'):
            # TODO get transaction id and verified status
            if 'status' == True:
                pass
            # TODO accept transaction and do the money work and change checking
            else:
                pass
            # TODO deny transaction and don't do any money work and change checking

        elif request.POST.get('Customer selected'):
            # delete this customer
            customer = Customer()
            # TODO get customer from request
            return manager_customer_view(request, customer)

    transactions = get_null_verified_transaction()

    return render(request, 'manager_checking_transactions.html',
                  {'manager': manager, 'transactions': transactions})


@login_required
@manager_required
def manager_customer_view(request, customer):
    manager = get_object_or_404(Manager, pk=request.user.id)
    if request.method == 'POST':
        if request.POST.get('customer change submitted'):
            # TODO get customer changed as customer i dont know how and then delete the below line
            changed_customer = Customer()
            changed_customer.save()
            return manager_customers_list_view(request)

        elif request.POST.get('delete this shit customer'):
            # TODO get customer changed as customer i dont know how and then delete the below line
            shit_customer = Customer()
            Customer.objects.all().delete(shit_customer)
            return manager_customers_list_view(request)

    transactions = customer_all_transactions(customer)

    return render(request, 'manager_customer_transactions.html',
                  {'manager': manager, 'customer': customer, 'transactions': transactions})


@login_required
@manager_required
def manager_all_system_transactions_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    transactions = get_all_system_transactions()
    return render(request, 'manager_all_system_transactions.html',
                  {'manager': manager, 'transactions': transactions})


@login_required
@manager_required
def manager_employee_view(request, employee):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        if request.POST.get('employee change submitted'):
            # TODO get employee changed as employee i dont know how and then delete the below line
            changed_employee = Employee()
            changed_employee.save()
            return manager_employees_list_view(request)

        elif request.POST.get('delete this shit employee'):
            # TODO get employee changed as employee i dont know how and then delete the below line
            shit_employee = Employee()
            Employee.objects.all().delete(shit_employee)
            return manager_employees_list_view(request)

    transactions = get_all_employee_checked_checking_transaction(employee)
    return render(request, 'manager_employee_checked_ing_transactions.html',
                  {'manager': manager, 'employee': employee, 'transactions': transactions})


@login_required
@manager_required
def manager_employees_list_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        if request.POST.get('employee selected'):
            # TODO delete bellow line and get employee from ui
            employee = Employee()
            return manager_employee_view(request, employee)
    employees_list = Employee.objects.all()
    return render(request, 'manager_employees_list.html',
                  {'manager': manager, 'employees': employees_list})


@login_required
@manager_required
def manager_customers_list_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        if request.POST.get('customer selected'):
            # TODO delete bellow line and get customer from ui
            customer = Customer()
            return manager_customer_view(request, customer)
    customers_list = Customer.objects.all()
    return render(request, 'manager_customers_list.html',
                  {'manager': manager, 'customers': customers_list})
