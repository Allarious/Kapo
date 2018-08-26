from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.customer.forms.forms import EditUser, SendMessage
from apps.accounts.models import *
from apps.customer.forms.forms import EditUser
from apps.employee.forms import EditEmployeeProfile
from apps.employee.models import Employee
from apps.accounts.decorators import employee_required
from apps.transactions.functions import *
from apps.transactions.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
@employee_required
def employee_profile_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    return render(request, 'employee-profile.html', {'employee': employee, })


@login_required
@employee_required
def index(request):
    return render(request, 'employee_HomePage.html', {})


@login_required
@employee_required
def employee_check_transaction_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)

    if request.POST.get('checked transaction'):
        # TODO get transaction id and verified status
        if 'status' == True:
            pass
        # TODO accept transaction and do the money work
        else:
            pass
        # TODO deny transaction and don't do any money work

        return redirect('/employee/')

    elif request.POST.get('New Transaction'):
        transactions = get_null_verified_transaction(employee)

        return redirect('employee:employee_checking_transactions')

    elif request.POST.get('Customer selected'):
        # delete this customer
        customer = Customer()
        # TODO get customer from request
        return employee_transaction_owner_view(request, customer)

    else:

        transactions = get_employee_transactions(employee)

        return render(request, 'employee_checking_transactions.html',
                      {'employee': employee, 'transactions': transactions})


@login_required
@employee_required
def update_employee_profile(request):
    user = MyUser.objects.get(username=request.user.username)
    # customer = user.customer
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES)
        form = EditEmployeeProfile(request.POST)

        if user_form.is_valid() and form.is_valid():
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:

                            if attr == 'password':

                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])
            employee = Employee.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(employee, attr, form.data[attr])
            user.save()
            employee.save()
            return HttpResponseRedirect(reverse('employee:employee_profile'))

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = EditUser()
        form = EditEmployeeProfile()

    return render(request, 'employee_edit.html',
                  {'user_form': user_form, 'form': form})


@login_required
@employee_required
def employee_transaction_owner_view(request, customer):
    employee = get_object_or_404(Employee, pk=request.user.id)
    transactions = customer_all_transactions(customer)

    return render(request, 'employee_customer_transactions.html',
                  {'employee': employee, 'customer': customer, 'transactions': transactions})


@login_required
@employee_required
def employee_all_system_transactions_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    transactions = get_all_system_transactions()
    return render(request, 'employee_all_system_transactions.html',
                  {'employee': employee, 'transactions': transactions})
