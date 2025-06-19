from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            f'Support Request from {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent! We will respond within 24 hours.')
        return redirect('support')
    
    return render(request, 'help/support.html')