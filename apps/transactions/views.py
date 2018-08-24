from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.core.models import Configuration
from apps.customer.models import Customer
from .forms.forms import *
from apps.accounts.decorators import customer_required


@login_required
@customer_required
def customer_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_transactions.html', {'customer': customer, })


@login_required
@customer_required
def exam_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    exam_wage = float(Configuration.objects.get(key='exam wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ExamTransactionForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.owner = customer
            cost = exam.dollar_cost * exam_wage
            if customer.dollar_wallet < cost:
                form.add_error('dollar_cost',
                               'You need {} more dollars!'.format(cost - customer.dollar_wallet))
                return render(request, 'exam_transactions.html',
                              {'customer': customer, 'form': form, 'wage': exam_wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            exam.save()
            customer.dollar_wallet -= cost
            # TODO add money to manager
            customer.save()
            exam.paid = True
            exam.save()
            return redirect('/customer/')
    else:
        form = ExamTransactionForm()

    return render(request, 'exam_transactions.html',
                  {'customer': customer, 'form': form, 'wage': exam_wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


@login_required
@customer_required
def app_fee_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    fee_wage = float(Configuration.objects.get(key='exam wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ApplicationTuitionFeeTransactionForm(request.POST)
        if form.is_valid():
            fee = form.save(commit=False)
            fee.owner = customer
            if fee.dollar_cost > fee.euro_cost and fee.euro_cost == 0:
                cost = fee.dollar_cost * fee_wage

                if customer.dollar_wallet < cost:
                    form.add_error('dollar_cost',
                                   'You need {} more Dollars!'.format(cost - customer.dollar_wallet))
                    return render(request, 'fee_transactions.html',
                                  {'customer': customer, 'form': form, 'wage': fee_wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})
                fee.save()
                customer.dollar_wallet -= fee.dollar_cost
                customer.save()
                fee.paid = True
                fee.save()


            elif fee.euro_cost > fee.dollar_cost and fee.dollar_cost == 0:
                cost = fee.dollar_cost * fee_wage

                if customer.euro_wallet < cost:
                    form.add_error('euro_cost',
                                   'You need {} more Euros!'.format(cost - customer.euro_wallet))
                    return render(request, 'fee_transactions.html',
                                  {'customer': customer, 'form': form, 'wage': fee_wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})

                fee.save()
                customer.euro_wallet -= fee.euro_cost
                customer.save()
                fee.paid = True
                fee.save()
            else:
                form.add_error('dollar_cost', 'sth went wrong!')
                return render(request, 'fee_transactions.html',
                              {'customer': customer, 'form': form, 'wage': fee_wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            # TODO add money to manager

            return redirect('/customer/')
    else:
        form = ApplicationTuitionFeeTransactionForm()

    return render(request, 'fee_transactions.html',
                  {'customer': customer, 'form': form, 'wage': fee_wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


@login_required
@customer_required
def foreign_pay_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    foreign_wage = float(Configuration.objects.get(key='foreign wage').value)
    dollar_rate = int(Configuration.objects.get(key='dollar').value)
    euro_rate = int(Configuration.objects.get(key='euro').value)

    if request.method == 'POST':
        form = ForeignPaymentTransactionForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.owner = customer
            if pay.dollar_cost > pay.euro_cost and pay.euro_cost == 0:
                cost = pay.dollar_cost * foreign_wage

                if customer.dollar_wallet < cost:
                    form.add_error('dollar_cost',
                                   'You need {} more Dollars!'.format(cost - customer.dollar_wallet))
                    return render(request, 'foreign_pay_transaction.html',
                                  {'customer': customer, 'form': form, 'wage': foreign_wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})
                pay.save()
                customer.dollar_wallet -= pay.dollar_cost
                customer.save()
                pay.paid = True
                pay.save()


            elif pay.euro_cost > pay.dollar_cost and pay.dollar_cost == 0:
                cost = pay.dollar_cost * foreign_wage

                if customer.euro_wallet < cost:
                    form.add_error('euro_cost',
                                   'You need {} more Euros!'.format(cost - customer.euro_wallet))
                    return render(request, 'foreign_pay_transaction.html',
                                  {'customer': customer, 'form': form, 'wage': foreign_wage,
                                   'dollar_rate': dollar_rate,
                                   'euro_rate': euro_rate})

                pay.save()
                customer.euro_wallet -= pay.euro_cost
                customer.save()
                pay.paid = True
                pay.save()
            else:
                form.add_error('dollar_cost', 'sth went wrong!')
                return render(request, 'foreign_pay_transaction.html',
                              {'customer': customer, 'form': form, 'wage': foreign_wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            # TODO add money to manager

            return redirect('/customer/')
    else:
        form = ForeignPaymentTransactionForm()

    return render(request, 'foreign_pay_transaction.html',
                  {'customer': customer, 'form': form, 'wage': foreign_wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})
