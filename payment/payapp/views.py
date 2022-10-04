from json import dumps

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

import stripe
import os
stripe.api_key = 'sk_test_51Lo9uLEe2EKIxJhR0fqvhZqNSsC57K8szem4Icx0fFSQWP6Uf0xoLV8MRWkN06oy8XPhqdxzYO59UBUDZ98ZhO5D00XXJ2wTbc'
def index(request):
    return render(request, 'payapp/index.html', context={'id':'price_1LoAB9Ee2EKIxJhRaoN3G6zU'})


def buy(request, id):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price':'price_1LoAB9Ee2EKIxJhRaoN3G6zU',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
    )
    #return (checkout_session.id)
    #return redirect(checkout_session.url, code=303)
    return HttpResponse(f'{checkout_session.id}')

def item(request, id):
    return render(request, 'payapp/box.html', context={'id': id})