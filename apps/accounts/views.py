from django.core.mail import send_mail
from django.urls import reverse

from apps.accounts.forms.forms import CustomerSignUpForm, UserForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
from apps.transactions.models import *
from tahlil import settings


def index(request):
    return render(request, 'Home_page.html', {})


# TODO bayad in 404 ro dorost konim
def handler404(request):
    return render(request, '404.html', status=404)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        # user.refresh_from_db()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/index.html', {})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def sign_up(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        form = CustomerSignUpForm(request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            username = request.POST['username']
            password = request.POST['password']
            user.set_password(user.password)
            user.is_customer = True
            user.save()
            customer = form.save(commit=False)
            customer.user = user
            customer.save()
            user = authenticate(username=username, password=password)
            if user is not None and customer is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accounts:customer_home'))

        else:
            # print(form)
            # print(user_form)
            print(user_form.errors, form.errors)
            return render(request, 'SignUp1.html',
                          {'user_form': user_form, 'form': form})

    else:
        user_form = UserForm()
        form = CustomerSignUpForm()
    return render(request, 'SignUp1.html',
                  {'user_form': user_form, 'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_customer:
                    login(request, user)
                    return HttpResponseRedirect(reverse('customer:customer_profile'))
                if user.is_manager:
                    login(request, user)
                    return HttpResponseRedirect(reverse('manager:manger_profile'))
                if user.is_employee:
                    login(request, user)
                    return HttpResponseRedirect(reverse('employee:employee_profile'))
            else:
                return render(request, 'Login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Login.html', {'error_message': 'Invalid login'})
    return render(request, 'Login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))


def transaction_report_email(request, transaction, customer):
    subject = 'Transaction report'
    message = 'Hello ' + customer.first_name + '\n'

    if isinstance(transaction, RialWalletIncTransaction):

        message += 'You had successfully increased your Rial wallet by ' + str(
            transaction.amount) + '.'

    elif isinstance(transaction, CurrencyConvertTransaction):

        message += 'You had successfully converted ' + str(transaction.amount) + ' ' + str(
            transaction.currency) + ' and paid ' + str(transaction.rial_cost) + ' Rials.'

    elif isinstance(transaction, ExamTransaction):

        message += 'Your ' + transaction.exam_title + ' exam '

        if transaction.verified:
            message += 'successfully verified and ' + str(
                transaction.dollar_cost) + '$ has been withdrawn from your account.'
        else:
            message += 'unfortunately not verified.\nHope to see you again.'


    elif isinstance(transaction, ApplicationTuitionFeeTransaction):

        message += 'Your ' + transaction.fee_type + 'request, '

        if transaction.verified:
            message += 'successfully verified and '

            if transaction.dollar_cost > 0:

                message += str(transaction.dollar_cost) + '$ has been withdrawn from your account.'

            else:
                message += str(transaction.euro_cost) + '€ has been withdrawn from your account.'

        else:
            message += 'unfortunately not verified.\nHope to see you again.'

    elif isinstance(transaction, ForeignPaymentTransaction):

        message += 'Your foreign payment request to ' + str(transaction.foreign_card_number) + ' bank account, '

        if transaction.verified:

            message += 'successfully verified and '

            if transaction.dollar_cost > 0:
                message += str(transaction.dollar_cost) + '$ has been withdrawn from your account.'
            else:
                message += str(transaction.euro_cost) + '€ has been withdrawn from your account.'

        else:

            message += 'unfortunately not verified.\nHope to see you again.'

    elif isinstance(transaction, DomesticPaymentTransaction):

        message += 'Your domestic payment request to ' + str(transaction.domestic_card_number) + ' bank account, '

        if transaction.verified:

            message += 'successfully verified and ' + str(
                transaction.rial_cost) + 'Rials has been withdrawn from your account.'

        else:
            message += 'unfortunately not verified.\nHope to see you again.'

    elif isinstance(transaction, UnknownPaymentTransaction):

        message += 'Your unknown payment request to ' + str(transaction.domestic_card_number) + ' bank account, '

        if transaction.verified:

            message += 'successfully verified and ' + str(
                transaction.rial_cost) + 'Rials has been withdrawn from your account.'

        else:
            message += 'unfortunately not verified.\nHope to see you again.'

    message += '\n Your transaction ID is ' + str(transaction.id)
    message += '\nThanks for using our site'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(customer.email), ]
    send_mail(subject, message, email_from, recipient_list)
    # if redirect needed
    # return redirect('redirect to a new page')


def inform_email(request, inform):
    subject = inform.subject
    message = inform.message
    recipient_list = []

    for customer in Customer.objects.all():
        if customer.email_notification:
            recipient_list.append(str(customer.email))


    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
    # if redirect needed
    # return redirect('redirect to a new page')


