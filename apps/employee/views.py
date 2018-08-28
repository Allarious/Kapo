from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.views import transaction_report_email
from apps.core.models import SystemAccounts
from apps.customer.forms.forms import EditUser, SendMessage
from apps.accounts.models import *
from apps.customer.forms.forms import EditUser
from apps.employee.forms import EditEmployeeProfile
from apps.employee.models import Employee
from apps.accounts.decorators import employee_required
from apps.manager.models import Manager
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
    transactions = get_employee_transactions(employee)

    if request.method == 'POST':
        # TODO check
        system_account = SystemAccounts.objects.all()[0]
        if request.POST.get('checked transaction'):
            transaction = transactions.pop(id=request.POST.get('transaction id', default=None))
            customer = transaction.owner
            status = request.POST.get('transaction status', default=False)
            if status == 'accepted':
                currency = transaction.currency_type
                if currency == 'rial':
                    system_account.rial_amount_account -= transaction.rial_cost
                    customer.rial_wallet -= transaction.rial_cost * transaction.wage_rate
                    customer.rial_wallet -= transaction.rial_cost
                    system_account.rial_amount_account += transaction.rial_cost * transaction.wage_rate

                elif currency == 'dollar':
                    system_account.dollar_amount_account -= transaction.dollar_cost
                    customer.dollar_wallet -= transaction.dollar_cost * transaction.wage_rate
                    customer.dollar_wallet -= transaction.dollar_cost
                    system_account.dollar_amount_account += transaction.dollar_cost * transaction.wage_rate
                elif currency == 'euro':
                    system_account.euro_amount_account -= transaction.euro_cost
                    customer.euro_wallet -= transaction.euro_cost * transaction.wage_rate
                    customer.euro_wallet -= transaction.euro_cost
                    system_account.euro_amount_account += transaction.euro_cost * transaction.wage_rate

                employees_wage = 0
                for employee in Employee.objects.all():
                    employees_wage += employee.wage_per_month
                if system_account.rial_amount_account <= 3 * employees_wage:
                    Notification(owner=Manager.objects.all()[0], type='insufficient money').save()

                system_account.save()
                customer.save()

                transaction.paid = True
                transaction.verified = True
                transaction.checking = False
                transaction_report_email(transaction, customer)

            elif status == 'rejected':
                transaction.paid = False
                transaction.checking = False
                transaction.verified = False
                transaction_report_email(transaction, customer)
            transaction.save()


        elif request.POST.get('Customer selected'):
            customer = Customer.objects.filter(username=request.POST.get('username'))
            return employee_transaction_owner_view(request, customer)

        # elif request.POST.get('assign'):
        #     transaction = get_null_verified_transactions()[0]
        #     transaction.checking_employee = employee
        #     transaction.checking = True
        #     return employee_check_transaction_view(request)

    # this will show manager not verified and not checked transactions

    return render(request, 'employee_transaction_check.html',
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


def employee_dashboard_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    notifications = Notification.objects.all().filter(owner=employee.user)
    notification = []
    for i in range(notifications.count()):
        notification.append(notifications[notifications.count() - 1 - i])
    Notification.objects.all().filter(owner=employee.user).update(seen=True)
    return render(request, 'employee_dashboard.html', {'notifications': notification})


def message_dashboard_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    messages = Message.objects.all().filter(receiver=employee.user)
    message = []
    for i in range(messages.count()):
        message.append(messages[messages.count() - 1 - i])
    return render(request, 'employee_massage_dashboard.html', {'messages': message})


def transaction_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    rial = RialWalletIncTransaction.objects.all().filter(owner=customer)
    exchange = CurrencyConvertTransaction.objects.all().filter(owner=customer)
    transactions = []
    transactions.extend(rial)
    transactions.extend(exchange)
    transactions.sort(key=lambda transaction: transaction.creation_time)
    transactions_list = []
    for transaction in transactions:
        tmp = []
        if isinstance(transaction, RialWalletIncTransaction):
            tmp.append('Rial Charge')
            tmp.append(str(transaction.amount) + 'ريال')
        elif isinstance(transaction, CurrencyConvertTransaction) and transaction.currency == 'dollar':
            tmp.append('Rial-Dollar Exchange')
            tmp.append(str(transaction.amount) + '$')
        else:
            tmp.append('Rial-Euro Exchange')
            tmp.append(str(transaction.amount) + '€')
        tmp.append(transaction.creation_time.date())
        tmp.append(transaction.creation_time.time())
        tmp.append(transaction.verified)
        tmp.append(transaction.description)
        transactions_list.append(tmp)
        order = False
        # TODO check order
    return render(request, 'transaction_dashboard.html', {'transactions': transactions_list,
                                                          'order': order})


def order_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    exam = ExamTransaction.objects.all().filter(owner=customer)
    apply = ApplicationTuitionFeeTransaction.objects.all().filter(owner=customer)
    foreign = ForeignPaymentTransaction.objects.all().filter(owner=customer)
    domestic = DomesticPaymentTransaction.objects.all().filter(owner=customer)
    unknown = UnknownPaymentTransaction.objects.all().filter(owner=customer)
    transactions = []
    transactions.extend(exam)
    transactions.extend(apply)
    transactions.extend(foreign)
    transactions.extend(domestic)
    transactions.extend(unknown)
    transactions.sort(key=lambda transaction: transaction.creation_time)
    transactions_list = []
    for transaction in transactions:
        tmp = []
        if isinstance(transaction, ExamTransaction):
            tmp.append('Exam')
            tmp.append(str(transaction.dollar_cost) + '$')
            transaction.description += "Exam title is: " + transaction.exam_title
        elif isinstance(transaction, ApplicationTuitionFeeTransaction):
            if transaction.fee_type == 'application fee':
                tmp.append('Application Fee')
            else:
                tmp.append('Tuition Fee')
            if transaction.dollar_cost > 0:
                tmp.append(str(transaction.dollar_cost) + '$')
            else:
                tmp.append(str(transaction.euro_cost) + '€')
            transaction.description += "University site url is: " + transaction.site_url
        elif isinstance(transaction, ForeignPaymentTransaction):
            tmp.append('Foreign Payment')
            if transaction.dollar_cost > 0:
                tmp.append(str(transaction.dollar_cost) + '$')
            else:
                tmp.append(str(transaction.euro_cost) + '€')
            transaction.description += "Destination card number is:" + transaction.foreign_card_number
        elif isinstance(transaction, DomesticPaymentTransaction):
            tmp.append('Domestic Payment')
            tmp.append(str(transaction.rial_cost) + 'ريال')
            transaction.description += "Destination card number is:" + transaction.domestic_card_number
        else:
            tmp.append('Unknown Payment')
            tmp.append(str(transaction.rial_cost) + 'ريال')
            transaction.description += "Destination card number is:" + transaction.domestic_card_number
        tmp.append(transaction.creation_time.date())
        tmp.append(transaction.creation_time.time())
        tmp.append(transaction.verified)
        tmp.append(transaction.description)
        transactions_list.append(tmp)
    return render(request, 'transaction_dashboard.html', {'transactions': transactions_list,
                                                          'order': True})


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
