from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from policies.models import Policy

@login_required
def submit_claim(request):
    if request.method == 'POST':
        messages.success(request, 'Claim submitted successfully!')
        return redirect('claim_success')
    return render(request, 'claims/submit.html')

@login_required
def claim_success(request):
    return render(request, 'claims/success.html')