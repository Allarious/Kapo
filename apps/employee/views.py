from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.employee.models import Employee
from apps.accounts.decorators import employee_required
from apps.transactions.models import *


@login_required
@employee_required
def employee_profile_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)
    return render(request, 'employee-profile.html', {'employee': employee, })


@login_required
@employee_required
def index(request):
    return render(request, 'employee_HomePage.html', {})


@login_required
@employee_required
def employee_check_transaction_view(request):
    employee = get_object_or_404(Employee, pk=request.user.id)

    if request.POST.get('checked transaction'):
        # TODO get transaction id and verified status
        if 'status' == True:
            pass
        # TODO accept transaction and do the money work
        else:
            pass
        # TODO deny transaction and dont do any money work

    else:

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

        return render(request, 'employee_checking_transactions.html',
                      {'employee': employee, 'transactions': transactions})
