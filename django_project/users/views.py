from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created successfully! You can now login into your account.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})