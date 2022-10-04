from django import HttpResponse
from django import render

import stripe
import environ

env = environ.Env()
environ.Env.read_env()

stripe.api_key = env('api_key')
def index(request):
    return render(request, 'payapp/index.html', context={'id':'price_1LoAB9Ee2EKIxJhRaoN3G6zU'})


def buy(request, id):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': id,
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