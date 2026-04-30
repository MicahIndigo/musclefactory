import stripe, json
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from profiles.models import Profile

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': 'Gym Membership',
                },
                'unit_amount': 1500, # £15
            },
            'quantity': 1,
        }],
        mode='payment',

        # Success and cancel URLS (local server)
        success_url='https://musclefactory.onrender.com/checkout/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://musclefactory.onrender.com/classes/',
    )


    return redirect(session.url, code=303)


@login_required
def checkout_success(request):
    profile = Profile.objects.get(user=request.user)
    profile.is_member = True
    profile.save()

    return redirect('class_list')
