from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dummy_payment import process_payment as dummy_process_payment  # Import from your library

@login_required
def process_payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        card_number = request.POST.get('card_number') 
        expiry = request.POST.get('card_expiry')
        cvv = request.POST.get('card_cvv')
        payment_method = request.POST.get('payment_method')

        payment_details = dummy_process_payment(float(amount), payment_method)

        context = {
            'transaction_id': payment_details.get('transaction_id'),
            'amount': amount,
            'is_successful': payment_details.get('is_successful'),
            'payment_method': payment_method,
            'card_number': card_number[-4:], 
            'expiry': expiry
        }
        return render(request, 'payment/result.html', context)

    return render(request, 'payment/form.html')
