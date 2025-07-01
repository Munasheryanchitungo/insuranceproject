from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string
from .models import Payment
from policies.models import Policy
from datetime import datetime, timedelta

@login_required
def process_payment(request):
    if request.method == 'POST':
        policy_type = request.POST.get('policy_type')
        
        # Set prices for policies
        prices = {
            'fire': 2,
            'theft': 2.5,
            'comprehensive': 6,
            'health': 5
        }
        amount = prices.get(policy_type, 0)
        
        if not policy_type or amount == 0:
            messages.error(request, 'Invalid policy type selected.')
            return redirect('policy_list')
        
        # Create Policy for the user
        policy = Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
            is_active=True
        )
        
        # Generate fake transaction ID
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        # Create payment record
        Payment.objects.create(
            user=request.user,
            policy_id=policy.id,
            amount=amount,
            payment_method='mobile_money',
            transaction_id=transaction_id,
            is_successful=True
        )
        
        messages.success(request, f'Payment successful! Policy #{policy.id} activated.')
        return redirect('dashboard')
    
    # If GET request
    return redirect('policy_list')
