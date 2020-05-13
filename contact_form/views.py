from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm
from .forms import ContactFormForm
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string

# Create your views here.

def contactForm(request):
    if request.method == "POST":
        contact_form = ContactFormForm(request.POST)

        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.save()

            send_mail(
                'RDNET - You have Message',
                'You have a message',
                'noreply@robert-davies.net',
                ['rob.davies1991@gmail.com'],
                fail_silently=False,
                html_message = render_to_string(
                    template_name='contactform/contact_email.html'
                ),
            )
            messages.success(request, "Form submitted successfully")
            return redirect('home')

    else:
        contact_form = ContactFormForm()

    return render(request, "contact_form.html", {'contact_form': contact_form})