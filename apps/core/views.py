from django.shortcuts import render


def contact_us_view(request):
    return render(request, 'contact_us.html', {})


def about_us_view(request):
    return render(request, 'about_us.html', {})


def policy_view(request):
    return render(request, 'policy.html', {})
