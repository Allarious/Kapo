from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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
    exam_wage = Configuration.objects.get(key='exam wage')
    dollar_rate = Configuration.objects.get(key='dollar')
    euro_rate = Configuration.objects.get(key='euro')

    if request.method == 'POST':
        form = ExamTransactionForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.dollar_cost = form.cleaned_data['dollar_cost']
            exam.owner = customer

            if customer.dollar_wallet < exam.dollar_cost:
                form.add_error('dollar_cost',
                               'You need {} more dollars!'.format(exam.dollar_cost - customer.dollar_wallet))
                return render(request, 'exam_transactions.html',
                              {'customer': customer, 'form': form, 'exam_wage': exam_wage,
                               'dollar_rate': dollar_rate,
                               'euro_rate': euro_rate})
            exam.save()
            customer.dollar_wallet -= exam.dollar_cost
            customer.save()
            exam.paid = True
            exam.save()
            return redirect('/customer/')
    else:
        form = ExamTransactionForm()

    return render(request, 'exam_transactions.html',
                  {'customer': customer, 'form': form, 'exam_wage': exam_wage, 'dollar_rate': dollar_rate,
                   'euro_rate': euro_rate})


def app_fee_transactions_view(request):
    pass