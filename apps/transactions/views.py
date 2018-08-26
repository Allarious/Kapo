from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.core.models import Configuration
from apps.manager.models import Manager
from .forms.forms import *
from apps.accounts.decorators import customer_required, manager_required


@login_required
@customer_required
def customer_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_transactions.html', {'customer': customer, })


# TODO update lahze yi maghdar e motanazer java script
@login_required
@customer_required
def customer_exchange_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    dollar_rate = float(Configuration.objects.get(key='dollar').value)
    euro_rate = float(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        exchange_form = Exchange2Form(request.POST)
        form = RialIncForm(request.POST)
        if exchange_form.is_valid() and form.is_valid():
            exchange = CurrencyConvertTransaction()
            exchange.owner = customer
            if request.POST.get("rial_inc") == '':
                if form.is_valid():
                    transaction = RialWalletIncTransaction()
                    transaction.amount = form.cleaned_data['amount']
                    transaction.owner = customer
                    customer.rial_wallet += transaction.amount
                    customer.save()
                    transaction.paid = True
                    transaction.save()
                    return HttpResponseRedirect(reverse('customer:index'))
            if request.POST.get('euro_exchange') == '':
                exchange.currency = 'euro'
                exchange.amount = exchange_form.cleaned_data['euro_amount']
                cost = exchange.amount * euro_rate
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    exchange.rial_cost = cost
                    customer.euro_wallet += exchange.amount
                else:
                    exchange_form.add_error('euro_amount', 'موجودی کافی نیست')
                    return render(request, 'transactions.html', {'customer': customer,
                                                                 'exchange_form': exchange_form,
                                                                 'form': form,
                                                                 'dollar': dollar_rate,
                                                                 'euro': euro_rate,
                                                                 'is_manager': False})
            elif request.POST.get('dollar_exchange') == '':
                exchange.currency = 'dollar'
                exchange.amount = exchange_form.cleaned_data['dollar_amount']
                cost = exchange.amount * dollar_rate
                if customer.rial_wallet >= cost:
                    customer.rial_wallet -= cost
                    exchange.rial_cost = cost
                    customer.dollar_wallet += exchange.amount
                else:
                    exchange_form.add_error('dollar_amount', 'موجودی کافی نیست')
                    return render(request, 'transactions.html', {'customer': customer,
                                                                 'exchange_form': exchange_form,
                                                                 'form': form,
                                                                 'dollar': dollar_rate,
                                                                 'euro': euro_rate,
                                                                 'is_manager': False})

            customer.save()
            exchange.paid = True
            exchange.save()
            return HttpResponseRedirect(reverse('customer:index'))
    else:
        form = RialIncForm()
        exchange_form = ExchangeForm()

    return render(request, 'transactions.html', {'customer': customer,
                                                 'exchange_form': exchange_form,
                                                 'form': form,
                                                 'dollar': dollar_rate,
                                                 'euro': euro_rate, })


@login_required
@customer_required
def exam_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    wage = float(Configuration.objects.get(key='exam wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ExamTransactionForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.owner = customer
            exam.currency_type = 'dollar'
            cost = exam.dollar_cost * wage
            if customer.dollar_wallet < cost:
                form.add_error('dollar_cost',
                               'You need {} more dollars!'.format(cost - customer.dollar_wallet))
                return render(request, 'exam_transactions.html',
                              {'customer': customer, 'form': form, 'wage': wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            exam.save()
            return redirect('/customer/')
    else:
        form = ExamTransactionForm()

    return render(request, 'exam_transactions.html',
                  {'customer': customer, 'form': form, 'wage': wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


@login_required
@customer_required
def app_fee_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    wage = float(Configuration.objects.get(key='exam wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ApplicationTuitionFeeTransactionForm(request.POST)
        if form.is_valid():
            fee = form.save(commit=False)
            fee.owner = customer
            if fee.dollar_cost > fee.euro_cost and fee.euro_cost == 0:
                cost = fee.dollar_cost * wage
                fee.currency_type = 'dollar'

                if customer.dollar_wallet < cost:
                    form.add_error('dollar_cost',
                                   'You need {} more Dollars!'.format(cost - customer.dollar_wallet))
                    return render(request, 'fee_transactions.html',
                                  {'customer': customer, 'form': form, 'wage': wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})
                fee.save()


            elif fee.euro_cost > fee.dollar_cost and fee.dollar_cost == 0:
                cost = fee.dollar_cost * wage
                fee.currency_type = 'euro'

                if customer.euro_wallet < cost:
                    form.add_error('euro_cost',
                                   'You need {} more Euros!'.format(cost - customer.euro_wallet))
                    return render(request, 'fee_transactions.html',
                                  {'customer': customer, 'form': form, 'wage': wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})

                fee.save()
            else:
                form.add_error('dollar_cost', 'sth went wrong!')
                return render(request, 'fee_transactions.html',
                              {'customer': customer, 'form': form, 'wage': wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})

            return redirect('/customer/')
    else:
        form = ApplicationTuitionFeeTransactionForm()

    return render(request, 'fee_transactions.html',
                  {'customer': customer, 'form': form, 'wage': wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


@login_required
@customer_required
def foreign_pay_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    wage = float(Configuration.objects.get(key='foreign wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ForeignPaymentTransactionForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.owner = customer
            if pay.dollar_cost > pay.euro_cost and pay.euro_cost == 0:
                cost = pay.dollar_cost * wage
                pay.currency_type = 'dollar'

                if customer.dollar_wallet < cost:
                    form.add_error('dollar_cost',
                                   'You need {} more Dollars!'.format(cost - customer.dollar_wallet))
                    return render(request, 'foreign_pay_transaction.html',
                                  {'customer': customer, 'form': form, 'wage': wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})
                pay.save()


            elif pay.euro_cost > pay.dollar_cost and pay.dollar_cost == 0:
                cost = pay.dollar_cost * wage
                pay.currency_type = 'euro'

                if customer.euro_wallet < cost:
                    form.add_error('euro_cost',
                                   'You need {} more Euros!'.format(cost - customer.euro_wallet))
                    return render(request, 'foreign_pay_transaction.html',
                                  {'customer': customer, 'form': form, 'wage': wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})

                pay.save()

            else:
                form.add_error('dollar_cost', 'sth went wrong!')
                return render(request, 'foreign_pay_transaction.html',
                              {'customer': customer, 'form': form, 'wage': wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})

            return redirect('/customer/')
    else:
        form = ForeignPaymentTransactionForm()

    return render(request, 'foreign_pay_transaction.html',
                  {'customer': customer, 'form': form, 'wage': wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


@login_required
@customer_required
def domestic_pay_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    wage = float(Configuration.objects.get(key='domestic wage').value)
    if request.method == 'POST':
        form = DomesticPaymentTransactionForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.owner = customer
            pay.currency_type = 'rial'

            cost = pay.rial_cost * wage
            if customer.rial_wallet < cost:
                form.add_error('rial_cost',
                               'You need {} more Rials!'.format(cost - customer.dollar_wallet))
                return render(request, 'domestic_pay_transaction.html',
                              {'customer': customer, 'wage': wage, 'form': form})
            pay.save()
            return redirect('/customer/')
    else:
        form = DomesticPaymentTransactionForm()

    return render(request, 'domestic_pay_transaction.html',
                  {'customer': customer, 'wage': wage, 'form': form})


@login_required
@customer_required
def unknown_pay_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    wage = float(Configuration.objects.get(key='domestic wage').value)

    if request.method == 'POST':
        form = UnknownPaymentTransactionForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.owner = customer
            cost = pay.rial_cost * wage
            pay.currency_type = 'rial'

            if customer.rial_wallet < cost:
                form.add_error('rial_cost',
                               'You need {} more Rials!'.format(cost - customer.dollar_wallet))
                return render(request, 'unknown_pay_transaction.html',
                              {'customer': customer, 'wage': wage, 'form': form})
            pay.save()

            # TODO Reza add new customer if we dont have the user

            return redirect('/customer/')
    else:
        form = UnknownPaymentTransactionForm()

    return render(request, 'unknown_pay_transaction.html',
                  {'customer': customer, 'wage': wage, 'form': form})


@login_required
@manager_required
def manager_exchange_view(request):
    manager = get_object_or_404(Manager, pk=request.user.id)
    customer = get_object_or_404(Customer, pk=request.user.id)
    dollar_rate = float(Configuration.objects.get(key='dollar').value)
    euro_rate = float(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        exchange_form = Exchange2Form(request.POST)
        form = RialIncForm(request.POST)
        if exchange_form.is_valid() and form.is_valid():
            exchange = CurrencyConvertTransaction()
            exchange.owner = customer
            if request.POST.get("rial_inc") == '':
                if form.is_valid():
                    transaction = RialWalletIncTransaction()
                    transaction.amount = form.cleaned_data['amount']
                    transaction.owner = customer
                    manager.system_accounts.rial_amount_account += transaction.amount
                    manager.system_accounts.save()
                    transaction.paid = True
                    transaction.save()
                    return HttpResponseRedirect(reverse('manager:index'))
            if request.POST.get('euro_exchange') == '':
                exchange.currency = 'euro'
                exchange.amount = exchange_form.cleaned_data['euro_amount']
                cost = exchange.amount * euro_rate
                if manager.system_accounts.rial_amount_account >= cost:
                    manager.system_accounts.rial_amount_account -= cost
                    exchange.rial_cost = cost
                    manager.system_accounts.euro_amount_account += exchange.amount
                else:
                    exchange_form.add_error('euro_amount', 'موجودی کافی نیست')
                    return render(request, 'transactions.html', {'customer': manager,
                                                                 'exchange_form': exchange_form,
                                                                 'form': form,
                                                                 'dollar': dollar_rate,
                                                                 'euro': euro_rate,
                                                                 'is_manager': True})
            elif request.POST.get('dollar_exchange') == '':
                exchange.currency = 'dollar'
                exchange.amount = exchange_form.cleaned_data['dollar_amount']
                cost = exchange.amount * dollar_rate
                if manager.system_accounts.rial_amount_account >= cost:
                    manager.system_accounts.rial_amount_account -= cost
                    exchange.rial_cost = cost
                    manager.system_accounts.dollar_amount_account += exchange.amount
                else:
                    exchange_form.add_error('dollar_amount', 'موجودی کافی نیست')
                    return render(request, 'transactions.html', {'customer': manager,
                                                                 'exchange_form': exchange_form,
                                                                 'form': form,
                                                                 'dollar': dollar_rate,
                                                                 'euro': euro_rate, })

            manager.system_accounts.save()
            exchange.paid = True
            exchange.save()
            return HttpResponseRedirect(reverse('manager:index'))
    else:
        form = RialIncForm()
        exchange_form = ExchangeForm()

    return render(request, 'transactions.html', {'customer': manager,
                                                 'exchange_form': exchange_form,
                                                 'form': form,
                                                 'dollar': dollar_rate,
                                                 'euro': euro_rate,
                                                 'is_manager': True})
