from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Policy
from datetime import date

@login_required
def dashboard(request):
    active_policies = Policy.objects.filter(
        user=request.user,
        is_active=True,
        end_date__gte=date.today()  # Only show non-expired policies
    ).order_by('policy_type')
    
    return render(request, 'dashboard.html', {
        'active_policies': active_policies,
        'policies_exist': active_policies.exists()
    })