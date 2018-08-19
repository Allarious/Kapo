from django.shortcuts import render, get_object_or_404

from apps.customer.models import Customer


def profile_view(request):
    customer = get_object_or_404(Customer, pk=request.user.id)
    return render(request, 'customer_profile.html', {'customer': customer,
                                                     })

# def customer_home_view(request,)