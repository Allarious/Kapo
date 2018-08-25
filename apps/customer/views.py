from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.core.models import Configuration
from apps.customer.forms.forms import *
from apps.customer.models import Customer
from apps.accounts.decorators import customer_required
from django.urls import reverse
from apps.transactions.models import *
from apps.accounts.models import *


@login_required
@customer_required
def index(request):
    return render(request, 'Customer_HomePage.html', {})


# TODO badan fieldash kamel beshan tebghe model

@login_required
@customer_required
def update_customer_profile(request):
    user = MyUser.objects.get(username=request.user.username)
    # customer = user.customer
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES)
        form = EditCustomerProfile(request.POST)

        if user_form.is_valid() and form.is_valid():
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:

                            if attr == 'password':

                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])
            customer = Customer.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(customer, attr, form.data[attr])
            user.save()
            customer.save()
            return HttpResponseRedirect(reverse('customer:customer profile'))

        else:
            print(user_form.errors, form.errors)
            return render(request, 'customer_update.html',
                          {'user_form': user_form, 'form': form})

    else:
        user_form = EditUser()
        form = EditCustomerProfile()

    return render(request, 'customer_update.html',
                  {'user_form': user_form, 'form': form})


@login_required
@customer_required
def customer_profile_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'Profile.html', {'customer': customer, })


@login_required
@customer_required
def customer_home_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    karmozds = Configuration.objects.exclude(key='dollar').exclude(key='euro')
    dollar_rate = Configuration.objects.get(key='dollar')
    euro_rate = Configuration.objects.get(key='euro')
    return render(request, 'customer_home.html',
                  {'customer': customer, 'karmozds': karmozds, 'euro_rate': euro_rate, 'dollar_rate': dollar_rate})


def customer_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    if request.method == 'POST':

        if request.POST.get('transactions button'):
            # list of all transactions
            transactions = customer_all_transactions(customer)

            return render(request, 'customer_dashboard.html',
                          {'customer': customer, 'transactions': transactions})

        elif request.POST.get('messages button'):
            # TODO Reza messago bezan
            pass

        elif request.POST.get('orders button'):
            # list of all transactions that needed or needs verification
            transactions = customer_order_transactions(customer)

            return render(request, 'customer_dashboard.html',
                          {'customer': customer, 'transactions': transactions})


def customer_all_transactions(customer):
    transactions = []
    # Rial increase transactions:
    rial_incs = RialWalletIncTransaction.objects.all().filter(owner=customer)
    # Convert transactions:
    converts = CurrencyConvertTransaction.objects.all().filter(owner=customer)
    # Exam transactions:
    exams = ExamTransaction.objects.filter(owner=customer)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(owner=customer)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(owner=customer)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(owner=customer)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(owner=customer)

    # for list of transactions uncomment bellow

    transactions.extend(rial_incs)
    transactions.extend(converts)
    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    # for lisf of lists of defferent transactions type uncomment beloq

    # transactions.append(rial_incs)
    # transactions.append(converts)
    # transactions.append(exams)
    # transactions.append(fees)
    # transactions.append(foreign_payments)
    # transactions.append(domestic_payments)
    # transactions.append(unknown_payments)

    #

    for transaction in transactions:
        transaction.is_one_day_passed()

    return transactions


def customer_order_transactions(customer):
    transactions = []

    # Exam transactions:
    exams = ExamTransaction.objects.filter(owner=customer)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(owner=customer)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(owner=customer)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(owner=customer)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(owner=customer)

    # for list of transactions uncomment bellow

    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    # for lisf of lists of defferent transactions type uncomment beloq

    # transactions.append(rial_incs)
    # transactions.append(converts)
    # transactions.append(exams)
    # transactions.append(fees)
    # transactions.append(foreign_payments)
    # transactions.append(domestic_payments)
    # transactions.append(unknown_payments)

    #

    for transaction in transactions:
        transaction.is_one_day_passed()

    return transactions


def send_message(request):
    user = MyUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = SendMessage(request.POST)

        if form.is_valid():
            message = Message()
            receiver = form.cleaned_data['receiver']
            message_receiver = MyUser.objects.get(username=receiver)
            message.receiver = message_receiver
            message.sender = user
            message.subject = form.cleaned_data['subject']
            message.message = form.cleaned_data['message']
            message.save()
            if user.is_customer:
                return HttpResponseRedirect(reverse('customer:index'))
            elif user.is_employee:
                return HttpResponseRedirect(reverse('employee:index'))
            else:
                return HttpResponseRedirect(reverse('manager:index'))

        else:
            print(form.errors)
            return render(request, 'send_message.html',
                          {user: 'user', 'form': form})

    else:
        form = SendMessage()

    return render(request, 'send_message.html',
                  {user: 'user', 'form': form})