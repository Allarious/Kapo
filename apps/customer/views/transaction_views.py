from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import Configuration, ExamTransaction
from apps.customer.models import Customer
from apps.core.forms.transaction_forms import *


@login_required
def customer_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_transactions.html', {'customer': customer, })


@login_required
def customer__transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_transactions.html', {'customer': customer, })


@login_required
def exam_transactions_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    exam_wage = Configuration.objects.get(key='exam wage')
    dollar_rate = Configuration.objects.get(key='dollar')
    euro_rate = Configuration.objects.get(key='euro')

    if request.method == 'POST':
        form = ExamTransactionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.dollar_cost = form.cleaned_data['dollar_cost']
            # print(form.owner)
            form.owner = customer
            # print(form.owner.user_id)

            if customer.dollar_wallet < form.dollar_cost:
                form.add_error('dollar_cost',
                               'You need {} more dollars!'.format(form.dollar_cost - customer.dollar_wallet))
                return render(request, 'exam_transactions.html',
                              {'customer': customer, 'form': form, 'exam_wage': exam_wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            form.save()
            return HttpResponseRedirect('/customer/')
    else:
        form = ExamTransactionForm()

    return render(request, 'exam_transactions.html',
                  {'customer': customer, 'form': form, 'exam_wage': exam_wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})
