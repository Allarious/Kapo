from django.shortcuts import render, get_object_or_404

from apps.customer.models import Customer


def profile_view(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'customer_profile.html', {'customer': customer,
                                            })
