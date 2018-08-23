from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import Configuration
from apps.customer.forms.currency_forms import RialIncForm, ExchangeForm
from apps.customer.models import Customer


@login_required
def customer_profile_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_profile.html', {'customer': customer, })


@login_required
def customer_home_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    karmozds = Configuration.objects.exclude(key='dollar').exclude(key='euro')
    karmozds = Configuration.objects.all()
    return render(request, 'customer_home.html', {'customer': customer, 'karmozds': karmozds})


@login_required
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
                cost = amount * int(euro_rate.value)
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    customer.euro_wallet += int(amount)
                else:
                    form.add_error('amount', 'not enough money')
                    return render(request, 'customer_exchange.html', {'customer': customer,
                                                                      'form': form,
                                                                      'dollar': dollar_rate,
                                                                      'euro': euro_rate, })
            elif currency[0] == 'dollar':
                cost = amount * int(dollar_rate.value)
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    customer.dollar_wallet += int(amount)
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
