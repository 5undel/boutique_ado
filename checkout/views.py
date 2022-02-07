from django.shortcuts import render, redirect, reverse
from django.contrib import messages  


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51KQcXaCY8qeh0zkCQYM7m8mm0nKlvCZ52fsAzxn6YJB6xr5V3O3vzAnZb4tdXBkH9sK22T06sFFzvjm7eTbsBgN1005hbRsGDk',
        
    }

    return render(request, template, context)