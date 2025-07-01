from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string

@login_required
def initiate_payment(request):
    if request.method == 'POST':
        policy_type = request.POST.get('policy_type')
        
        # Get policy price (replace with your actual prices)
        prices = {
            'fire': 2,
            'theft': 2.5,
            'comprehensive': 6,
            'health': 5
        }
        
        # Create policy record
        policy = Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            is_active=False  # Will activate after payment
        )
        
        
        # Create payment
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        from .models import Payment
        Payment.objects.create(
            user=request.user,
            policy_id=policy.id,
            amount=amount,
            payment_method='mobile_money',
            transaction_id=transaction_id,
            is_successful=True
        )
        
        messages.success(request, f'Payment successful! Policy #{policy.id} activated.')
        return redirect('policy_list')
    
    return redirect('dashboard')