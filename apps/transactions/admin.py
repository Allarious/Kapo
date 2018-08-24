from django.contrib import admin
from .models import *


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'paid')


class AppTransactionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'fee_type', 'paid')


admin.site.register(ExamTransaction, TransactionAdmin)
admin.site.register(ApplicationTuitionFeeTransaction, AppTransactionAdmin)
admin.site.register(DomesticPaymentTransaction, TransactionAdmin)
admin.site.register(ForeignPaymentTransaction, TransactionAdmin)
admin.site.register(UnknownPaymentTransaction, TransactionAdmin)
