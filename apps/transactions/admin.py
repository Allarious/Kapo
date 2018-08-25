from django.contrib import admin
from .models import *


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'paid')


class AppTransactionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'fee_type', 'paid')


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'currency', 'amount', 'paid')


class RialWalletIncAdmin(admin.ModelAdmin):
    list_display = ('owner', 'amount', 'paid')


admin.site.register(CurrencyConvertTransaction, ExchangeAdmin)
admin.site.register(RialWalletIncTransaction, RialWalletIncAdmin)
admin.site.register(ExamTransaction, TransactionAdmin)
admin.site.register(ApplicationTuitionFeeTransaction, AppTransactionAdmin)
admin.site.register(DomesticPaymentTransaction, TransactionAdmin)
admin.site.register(ForeignPaymentTransaction, TransactionAdmin)
admin.site.register(UnknownPaymentTransaction, TransactionAdmin)
