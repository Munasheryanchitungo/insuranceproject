# payments/views.py
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, random, string
from datetime import datetime, timedelta
from policies.models import Policy
from .models import Payment

@csrf_exempt
@login_required
def process_payment_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        policy_type = data.get('policy_type')
        
        prices = {
            'fire': 2,
            'theft': 2.5,
            'comprehensive': 6,
            'health': 5
        }
        amount = prices.get(policy_type, 0)
        
        # Create policy
        policy = Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
            is_active=True
        )
        
        # Create payment record
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        Payment.objects.create(
            user=request.user,
            policy_id=policy.id,
            amount=amount,
            payment_method='mobile_money',
            transaction_id=transaction_id,
            is_successful=True
        )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Payment completed. {policy.get_policy_type_display()} policy activated.',
            'policy_id': policy.id
        })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
