from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def userControlPanel(request):

    user = User.objects.get(email=request.user.email)

    return render(request, "ucp.html", {"profile": user})