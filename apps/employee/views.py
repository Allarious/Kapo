from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.customer.forms.forms import EditUser, SendMessage
from apps.accounts.models import *
from apps.customer.forms.forms import EditUser
from apps.customer.views import customer_all_transactions
from apps.employee.forms import EditEmployeeProfile
from apps.employee.models import Employee
from apps.accounts.decorators import employee_required
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


def get_null_verified_transaction(employee):
    transactions = []
    # Exam transactions:
    exams = ExamTransaction.objects.filter(checking=False, verified=None)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(checking=False, verified=None)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(checking=False, verified=None)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(checking=False, verified=None)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(checking=False, verified=None)

    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    for transaction in transactions:
        transaction.is_one_day_passed()
        if transaction.verified is False:
            transactions.pop(transaction)

    transactions.sort(key=lambda transaction: transaction.creation_time, reverse=True)
    transactions[0].checking_employee = employee
    transactions[0].checking = True
    return transactions


def get_employee_transactions(employee):
    transactions = []
    # Exam transactions:
    exams = ExamTransaction.objects.filter(checking_employee=employee, verified=None)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(checking_employee=employee, verified=None)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(checking_employee=employee, verified=None)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(checking_employee=employee, verified=None)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(checking_employee=employee, verified=None)

    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    for transaction in transactions:
        transaction.is_one_day_passed()
        if transaction.verified is False:
            transactions.pop(transaction)

    return transactions


def get_all_system_transactions():
    transactions = []
    # Rial increase transactions:
    rial_incs = RialWalletIncTransaction.objects.all()
    # Convert transactions:
    converts = CurrencyConvertTransaction.objects.all()
    # Exam transactions:
    exams = ExamTransaction.objects.all()
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.all()
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.all()
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.all()
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.all()

    # for list of transactions uncomment bellow

    transactions.extend(rial_incs)
    transactions.extend(converts)
    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    for transaction in transactions:
        transaction.is_one_day_passed()

    return transactions