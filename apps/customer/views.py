from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView

from apps.customer.forms.forms import RialIncForm
from apps.customer.models import Customer


@login_required
def customer_profile_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_profile.html', {'customer': customer, })


@login_required
def customer_home_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_home.html', {'customer': customer, })


@login_required




def customer_rial_inc_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    if request.method == 'POST':
        form = RialIncForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            customer.rial_wallet += amount
            customer.save()
            return HttpResponseRedirect('/customer/home/')
    else:
        form = RialIncForm()

    return render(request, 'customer_rial_wallet_inc.html', {'customer': customer, 'form': form})
