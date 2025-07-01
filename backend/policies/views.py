from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Policy
from datetime import datetime, timedelta

@login_required
def policy_list(request):
    policies = [
        {'type': 'fire', 'name': 'Fire Cover', 'price': 2},
        {'type': 'theft', 'name': 'Theft Protection', 'price': 2.5},
        {'type': 'comprehensive', 'name': 'Comprehensive', 'price': 6},
        {'type': 'health', 'name': 'Health Microinsurance', 'price': 5},
    ]
    return render(request, 'policies/list.html', {'policies': policies})

@login_required
def subscribe_policy(request):
    if request.method == 'POST':
        policy_type = request.POST.get('policy_type')
        Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
            is_active=True
        )
        messages.success(request, 'Policy subscribed successfully!')
    return redirect('policy_list')