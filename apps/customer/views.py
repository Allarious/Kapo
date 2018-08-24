from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import Configuration
from apps.customer.forms.currency_forms import *
from apps.customer.models import Customer
from apps.accounts.decorators import customer_required
from django.views.generic.edit import UpdateView
from django.urls import reverse


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


@login_required
@customer_required
def customer_rial_inc_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    if request.method == 'POST':
        form = RialIncForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            customer.rial_wallet += amount
            customer.save()
            return HttpResponseRedirect('/customer/')
    else:
        form = RialIncForm()

    return render(request, 'customer_rial_wallet_inc.html', {'customer': customer, 'form': form})


@login_required
@customer_required
def customer_exchange_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    dollar_rate = Configuration.objects.get(key='dollar')
    euro_rate = Configuration.objects.get(key='euro')
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            currency = form.cleaned_data['currency']
            if currency[0] == 'euro':
                cost = amount * float(euro_rate.value)
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    customer.euro_wallet += float(amount)
                else:
                    form.add_error('amount', 'not enough money')
                    return render(request, 'customer_exchange.html', {'customer': customer,
                                                                      'form': form,
                                                                      'dollar': dollar_rate,
                                                                      'euro': euro_rate, })
            elif currency[0] == 'dollar':
                cost = amount * float(dollar_rate.value)
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    customer.dollar_wallet += float(amount)
                else:
                    form.add_error('amount', 'not enough money')
                    return render(request, 'customer_exchange.html', {'customer': customer,
                                                                      'form': form,
                                                                      'dollar': dollar_rate,
                                                                      'euro': euro_rate, })

            customer.save()
            return HttpResponseRedirect('/customer/')
    else:
        form = ExchangeForm()

    return render(request, 'customer_exchange.html', {'customer': customer,
                                                      'form': form,
                                                      'dollar': dollar_rate,
                                                      'euro': euro_rate, })


def customer_dashboard_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    if request.method == 'POST':
        if request.POST.get('transactions button'):
            pass
        # TODO one list or miltiple lists
        elif request.POST.get('messages button'):
            # TODO Reza messago bezan
            pass
        elif request.POST.get('orders button'):
            # TODO DUDU WTF?
            pass
