from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Policy
from datetime import datetime, timedelta

@login_required
def dashboard(request):
    # Get active policies for the current user
    active_policies = Policy.objects.filter(
        user=request.user,
        is_active=True,
        end_date__gte=datetime.now().date()  # Only policies that haven't expired
    )
    return render(request, 'dashboard.html', {'active_policies': active_policies})

@login_required
def policy_list(request):
    available_policies = [
        {'type': 'fire', 'name': 'Fire Cover', 'price': 2},
        {'type': 'theft', 'name': 'Theft Protection', 'price': 2.5},
        {'type': 'comprehensive', 'name': 'Comprehensive', 'price': 6},
        {'type': 'health', 'name': 'Health Microinsurance', 'price': 5},
    ]
    return render(request, 'policies/list.html', {'policies': available_policies})

@login_required
def subscribe_policy(request):
    if request.method == 'POST':
        policy_type = request.POST.get('policy_type')
        
        # Create the policy with proper dates
        Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            start_date=datetime.now().date(),  # Use date() instead of datetime
            end_date=datetime.now().date() + timedelta(days=30),
            is_active=True
        )
        messages.success(request, 'Policy subscribed successfully!')
        return redirect('dashboard')  # Redirect to dashboard after subscription
    
    return redirect('policy_list')