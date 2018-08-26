from .models import *


def get_all_system_transactions():
    transactions = []
    # Rial increase transactions:
    rial_incs = RialWalletIncTransaction.objects.all()
    # Convert transactions:
    converts = CurrencyConvertTransaction.objects.all()
    # Exam transactions:
    exams = ExamTransaction.objects.all()
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.all()
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.all()
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.all()
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.all()

    # for list of transactions uncomment bellow

    transactions.extend(rial_incs)
    transactions.extend(converts)
    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    for transaction in transactions:
        transaction.is_one_day_passed()

    return transactions


def get_null_verified_transaction(employee):
    transactions = []
    # Exam transactions:
    exams = ExamTransaction.objects.filter(checking=False, verified=None)
    # Application and tuition fees transactions:
    fees = ApplicationTuitionFeeTransaction.objects.filter(checking=False, verified=None)
    # Foregin payments transactions:
    foreign_payments = ForeignPaymentTransaction.objects.filter(checking=False, verified=None)
    # Domestic transactions:
    domestic_payments = DomesticPaymentTransaction.objects.filter(checking=False, verified=None)
    #  Unknown payments transactions:
    unknown_payments = UnknownPaymentTransaction.objects.filter(checking=False, verified=None)

    transactions.extend(exams)
    transactions.extend(fees)
    transactions.extend(foreign_payments)
    transactions.extend(domestic_payments)
    transactions.extend(unknown_payments)

    for transaction in transactions:
        transaction.is_one_day_passed()
        if transaction.verified is False:
            transactions.pop(transaction)

    transactions.sort(key=lambda transaction: transaction.creation_time, reverse=True)
    transactions[0].checking_employee = employee
    transactions[0].checking = True
    return transactions


def get_employee_transactions(employee):
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

    return transactions


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

