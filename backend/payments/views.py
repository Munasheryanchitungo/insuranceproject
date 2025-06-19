from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string

@login_required
def process_payment(request):
    if request.method == 'POST':
        policy_type = request.POST.get('policy_type')
        
        # Get policy price
        prices = {
            'fire': 2,
            'theft': 2.5,
            'comprehensive': 6,
            'health': 5
        }
        amount = prices.get(policy_type, 0)
        
        # Create policy (import here to avoid circular import)
        from policies.models import Policy
        policy = Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            is_active=True
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
    
    return redirect('policy_list')