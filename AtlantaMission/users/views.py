from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewUser, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if(request.method == 'POST'):
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'We successfully added {first_name} to our Callodine family!')
            return redirect('login')
    else:
        form = NewUser()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if(request.method == 'POST'):
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            first_name = user_form.cleaned_data.get('first_name')
            messages.success(request, f'Hey {first_name}! Your profile has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)