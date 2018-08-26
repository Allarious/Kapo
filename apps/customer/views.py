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
    notifications = Notification.objects.all().filter(owner=customer.user)
    print(notifications[0].seen)
    print(notifications[1].seen)
    notification = []
    for i in range(notifications.count()):
        notification.append(notifications[notifications.count() - 1 - i])
    Notification.objects.all().filter(owner=customer.user).update(seen=True)
    return render(request, 'customer_dashboard1.html', {'notifications': notification})


def message_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    messages = Message.objects.all().filter(receiver=customer.user)
    message = []
    for i in range(messages.count()):
        message.append(messages[messages.count() - 1 - i])
    return render(request, 'customer_message_dashboard.html', {'messages': message})


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
    return render(request, 'transaction_dashboard.html', {'transactions': transactions_list,
                                                          'order' : order})


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
            if transaction.fee_type== 'application fee':
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

# def customer_dashboard_view(request):
#     customer = get_object_or_404(Customer, pk=request.user.id)
#     if request.method == 'POST':
#
#         if request.POST.get('transactions button'):
#             # list of all transactions
#             transactions = customer_all_transactions(customer)
# #
#             return render(request, 'customer_dashboard.html',
#                           {'customer': customer, 'transactions': transactions})
#
#         elif request.POST.get('messages button'):
#
#             pass
#
#         elif request.POST.get('orders button'):
#             # list of all transactions that needed or needs verification
#             transactions = customer_order_transactions(customer)
#
#             return render(request, 'customer_dashboard.html',
#                           {'customer': customer, 'transactions': transactions})


def send_message(request):
    user = get_object_or_404(MyUser, pk=request.user.id)
    # user = MyUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = SendMessage(request.POST)

        if form.is_valid():
            notification = Notification()
            message = Message()
            receiver = form.cleaned_data['receiver']
            message_receiver = get_object_or_404(MyUser, username=receiver)
            # message_receiver = MyUser.objects.get(username=receiver)
            message.receiver = message_receiver
            notification.owner = message_receiver
            notification.type = 'message'
            message.sender = user
            message.subject = form.cleaned_data['subject']
            message.message = form.cleaned_data['message']
            notification.save()
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
