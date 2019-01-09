from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from ..billing.models import BillingProfile
from .forms import AddressForm

# CRUD create update retrieve delete
def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():

        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        instance = form.save(commit=False)
 
        
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()

            request.session[address_type + '_address_id'] = instance.id
            # billing_address_id = request.session.get('billing_address_id', None)
            # shipping_address_id = request.session.get('shipping_address_id', None)
            print(address_type + '_address_id')
        else:
            print('Error Here')
            return redirect('cart:checkout')

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('cart:checkout')
    return redirect('cart:checkout')