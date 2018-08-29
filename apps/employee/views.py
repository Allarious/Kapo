from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.views import transaction_report_email
from apps.core.models import SystemAccounts
from apps.customer.forms.forms import EditUser, SendMessage
from apps.accounts.models import *
from apps.customer.forms.forms import EditUser
from apps.employee.forms import EditEmployeeProfile
from apps.employee.models import Employee
from apps.accounts.decorators import employee_required, employee_is_not_banned
from apps.manager.models import Manager
from apps.transactions.functions import *
from apps.transactions.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
@employee_required
@employee_is_not_banned
def employee_profile_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    return render(request, 'employee-profile.html', {'employee': employee, })


@login_required
@employee_required
def index(request):
    return render(request, 'employee_HomePage.html', {})


@login_required
@employee_required
@employee_is_not_banned
def employee_check_transaction_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    # transactions = get_employee_transactions(employee)
    transactions = get_all_system_transactions()
    transactions.sort(key=lambda transaction: transaction.creation_time, reverse=True)

    if request.method == 'POST':
        print(request.POST)
        # TODO check
        system_account = SystemAccounts.objects.all()[0]
        if request.POST.get('assign') == '':
            tmp = get_null_verified_transactions()
            print(tmp)
            if len(tmp) > 0:
                transaction = tmp[0]
                print(transaction)
                transaction.checking_employee = employee
                print(employee)
                transaction.checking = True
                transaction.save()
                return render(request, 'employee_transaction_check.html',
                              {'employee': employee, 'transactions': transactions, 'none': None})

        if request.POST.get('checked transaction'):
            transaction = transactions.pop(id=request.POST.get('transaction id', default=None))
            customer = transaction.owner
            status = request.POST.get('transaction status', default=False)
            if status == 'accept':
                currency = transaction.currency_type
                if currency == 'rial':
                    cost = transaction.rial_cost * transaction.wage_rate + transaction.rial_cost
                    if customer.rial_wallet < cost:
                        transaction.paid = False
                        transaction.checking = False
                        transaction.verified = False
                        transaction_report_email(transaction, customer)
                        return transaction.save()

                    customer.rial_wallet -= cost
                    system_account.rial_amount_account += round(transaction.rial_cost * transaction.wage_rate, 2)

                elif currency == 'dollar':
                    cost = transaction.dollar_cost * transaction.wage_rate + transaction.dollar_cost
                    if customer.dollar_wallet < cost:
                        transaction.paid = False
                        transaction.checking = False
                        transaction.verified = False
                        transaction_report_email(transaction, customer)
                        return transaction.save()
                    customer.dollar_wallet -= cost

                    system_account.dollar_amount_account += round(transaction.dollar_cost * transaction.wage_rate, 2)
                elif currency == 'euro':
                    cost = transaction.euro_cost * transaction.euro_cost + transaction.euro_cost
                    if customer.euro_wallet < cost:
                        transaction.paid = False
                        transaction.checking = False
                        transaction.verified = False
                        transaction_report_email(transaction, customer)
                        return transaction.save()
                    customer.euro_wallet -= cost
                    system_account.euro_amount_account += round(transaction.euro_cost * transaction.wage_rate, 2)

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

            elif status == 'reject':
                transaction.paid = False
                transaction.checking = False
                transaction.verified = False
                transaction_report_email(transaction, customer)
            transaction.save()

        if request.POST.get('Customer selected'):
            customer = Customer.objects.filter(username=request.POST.get('username'))
            return employee_transaction_owner_view(request, customer)



    return render(request, 'employee_transaction_check.html',
                  {'employee': employee, 'transactions': transactions, 'none': None})


@login_required
@employee_required
@employee_is_not_banned
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
@employee_is_not_banned
def employee_transaction_owner_view(request, customer):
    employee = get_object_or_404(Employee, pk=request.user.id)
    transactions = customer_all_transactions(customer)

    return render(request, 'employee_customer_transactions.html',
                  {'employee': employee, 'customer': customer, 'transactions': transactions})


@login_required
@employee_required
@employee_is_not_banned
def employee_all_system_transactions_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    transactions = get_all_system_transactions()
    return render(request, 'employee_all_system_transactions.html',
                  {'employee': employee, 'transactions': transactions})


@login_required
@employee_required
@employee_is_not_banned
def employee_dashboard_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    notifications = Notification.objects.all().filter(owner=employee.user)
    notification = []
    for i in range(notifications.count()):
        notification.append(notifications[notifications.count() - 1 - i])
    Notification.objects.all().filter(owner=employee.user).update(seen=True)
    return render(request, 'employee_dashboard.html', {'notifications': notification})


@login_required
@employee_required
@employee_is_not_banned
def message_dashboard_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    messages = Message.objects.all().filter(receiver=employee.user)
    message = []
    for i in range(messages.count()):
        message.append(messages[messages.count() - 1 - i])
    return render(request, 'employee_massage_dashboard.html', {'messages': message})


@login_required
@employee_required
@employee_is_not_banned
def transaction_dashboard_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    rial = RialWalletIncTransaction.objects.all()
    exchange = CurrencyConvertTransaction.objects.all()
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


def get_all_system_transactions():
    transactions = []
    # Rial increase transactions:
    rial_incs = RialWalletIncTransaction.objects.all().exclude(manager_owner=False)
    # Convert transactions:
    converts = CurrencyConvertTransaction.objects.all().exclude(manager_owner=False)
    # Exam transactions:
    exams = ExamTransaction.objects.all().exclude(manager_owner=False)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.all().exclude(manager_owner=False)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.all().exclude(manager_owner=False)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.all().exclude(manager_owner=False)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.all().exclude(manager_owner=False)

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


def get_null_verified_transactions():
    transactions = []
    # Exam transactions:
    exams = ExamTransaction.objects.filter(verified=None)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(verified=None)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(verified=None)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(verified=None)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(verified=None)

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
