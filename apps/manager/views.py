from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms.forms import UserForm, EmployeeSignUpForm
from apps.accounts.models import MyUser, Inform
from apps.accounts.views import inform_email
from apps.customer.models import Customer
from apps.manager.models import *
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
    transactions = get_null_verified_transactions()
    # TODO this above just gave without checking status but not verified

    if request.method == 'POST':
        # TODO check
        if request.POST.get('checked transaction'):
            transaction = transactions.pop(id=request.POST.get('transaction id', default=None))
            status = request.POST.get('transaction status', default=False)
            if status == 'accepted':
                # TODO how to know what kind of cost we have
                manager.system_accounts.dollar_amount_account -= transaction.dollar_cost
                manager.system_accounts.dollar_amount_account -= transaction.dollar_cost
                manager.system_accounts.rial_amount_account -= transaction.rial_cost
                employees_wage = 0
                for employee in Employee.objects.all():
                    employees_wage += employee.wage_per_month
                if manager.system_accounts.rial_amount_account <= employees_wage:
                    # TODO send notif be kossher
                    pass
                manager.system_accounts.save()

                transaction.paid = True
                transaction.verified = True

            elif status == 'rejected':
                transaction.paid = False
                transaction.checking = False
                transaction.verified = False
            transaction.save()


        elif request.POST.get('Customer selected'):
            # delete this customer
            # TODO get customer from request

            customer = Customer().objects.filter(username=request.POST.get('username'))
            return manager_customer_view(request, customer)

    # this will show manager not verified and not checked transactions

    return render(request, 'manager_checking_transactions.html',
                  {'manager': manager, 'transactions': transactions})


@login_required
@manager_required
def manager_customer_view(request, customer):
    manager = get_object_or_404(Manager, pk=request.user.id)
    if request.method == 'POST':
        if request.POST.get('delete this shit customer'):
            # TODO check
            shit_customer = Customer.objects.filter(username=request.username)
            Customer.objects.all().delete(shit_customer)
            return manager_customers_list_view(request)
        elif request.POST.get('send_message'):
            # TODO REZA send message gets customer id

            return HttpResponseRedirect(reverse('manager:send_message'))

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
    transactions = get_all_employee_checked_checking_transaction(employee)
    return render(request, 'manager_employee_checked_ing_transactions.html',
                  {'manager': manager, 'employee': employee, 'transactions': transactions})


@login_required
@manager_required
def manager_employees_list_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        # TODO check
        if request.POST.get('employee selected'):
            return manager_employee_view(request, Employee.objects.filter(username=request.username))

        elif request.POST.get('ban employee'):
            Employee.objects.filter(username=request.username).update(is_not_banned=False)

        elif request.POST.get('remove'):
            Employee.objects.all().delete(username=request.username)

        elif request.POST.get('wage has fucking changed'):
            Employee.objects.filter(username=request.username).update(wage_per_month=request.new_wage)
        elif request.POST.get('send_message'):
            # TODO REZA send message gets employee id
            return HttpResponseRedirect(reverse('manager:send_message'))

    employees_list = Employee.objects.all()
    return render(request, 'accounts.html',
                  {'manager': manager, 'accounts': employees_list})


@login_required
@manager_required
def manager_customers_list_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        # TODO check

        if request.POST.get('delete this shit customer'):
            Customer.objects.all().delete(username=request.username)
            request.success = True
        elif request.POST.get('opeen profle of customer'):

            return manager_customer_view(request, Customer.objects.filter(username=request.username))

    customers_list = Customer.objects.all()
    return render(request, 'accounts.html',
                  {'manager': manager, 'accounts': customers_list})


@login_required
@manager_required
def manager_add_employee(request):
    manager = get_object_or_404(Manager, pk=request.user.id)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            username = request.POST['username']
            password = request.POST['password']
            user.set_password(user.password)
            user.is_employee = True
            user.save()
            employee = form.save(commit=False)
            employee.user = user
            employee.save()
            user = authenticate(username=username, password=password)
            if user is not None and employee is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('manager:index'))

        else:

            return render(request, 'SignUp2.html',
                          {'manager': manager, 'user_form': user_form, 'form': form})

    else:
        user_form = UserForm()
        form = EmployeeSignUpForm()
    return render(request, 'SignUp2.html',
                  {'user_form': user_form, 'form': form})


@login_required
@manager_required
def manager_exams_list(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    exams = ManagerAddedExams.objects.all()
    if request.method == 'POST':
        if request.POST.get('exam added'):
            exam_image_url = request.POST.get('exam_image_url')
            exam_title = request.POST.get('exam_title')
            exam_site_url = request.POST.get('exam_site_url')
            exam_dollar_cost = request.POST.get('exam_dollar_cost')
            new_exam = ManagerAddedExams()
            new_exam.dollar_cost = exam_dollar_cost
            new_exam.site_url = exam_site_url
            new_exam.exam_title = exam_title
            new_exam.image_url = exam_image_url
            new_exam.save()

            return render(request, 'exams.html',
                          {'manger': manager, 'exams': exams})

        return render(request, 'exams.html',
                      {'manger': manager, 'exams': exams})


@login_required
@manager_required
def manager_send_to_all(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    if request.method == 'POST':
        if request.POST.get('sent to all'):
            inform = Inform(request.POST.get('subject'), request.POST.get('message')).save()
            inform_email(inform)

            return HttpResponseRedirect('manager:index')
    return render(request, 'sendtoall.html',
                  {'manger': manager})
