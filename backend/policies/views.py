from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Policy
from datetime import datetime, timedelta, date

@login_required
def dashboard(request):
    active_policies = Policy.objects.filter(
        user=request.user,
        is_active=True,
        end_date__gte=date.today()
    )
    return render(request, 'dashboard.html', {
        'active_policies': active_policies,
        'policies_exist': active_policies.exists()
    })

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
        Policy.objects.create(
            user=request.user,
            policy_type=policy_type,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=30),
            is_active=True
        )
        messages.success(request, 'Policy subscribed successfully!')
        return redirect('dashboard')
    return redirect('policy_list')

@login_required
def submit_claim(request):
    active_policies = Policy.objects.filter(
        user=request.user,
        is_active=True,
        end_date__gte=date.today()
    )
    return render(request, 'claims/submit.html', {
        'active_policies': active_policies
    })