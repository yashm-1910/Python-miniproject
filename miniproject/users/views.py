from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, VolunteerForm, AssistanceForm
from django.core.mail import send_mail, BadHeaderError
from django.http import request


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context) 

@login_required
def Volunteer(request):
    volunteer_form = VolunteerForm()
    if request.method == 'POST':
        form= VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('firstname') + " " + form.cleaned_data.get('lastname')
            message = 'Dear {},\nWe are reaching out to thank you for registering to volunteer to help cyclone victims.\nPlease feel free to share the event as our goal is to gather as many volunteers as possible.\nThank you again, and have great day!'.format(name)
            try:
                send_mail("Cyclone Tauktae Volunteer Registration", message, settings.EMAIL_HOST_USER, [email]) 
                messages.success(request, f'You have successfully registered!')
            except BadHeaderError:
                messages.error(request,f'Registration Unsucessful! Please Try Again')
            return redirect('volunteer')
        else:
            form = VolunteerForm()
    return render(request, 'users/volunteer.html', {'form': volunteer_form})

@login_required
def Assistance(request):
    assistance_form = AssistanceForm()
    if request.method == 'POST':
        form= AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            message = 'Thank you for contacting us.\nHelp will arrive for you shortly.'
            try:
                send_mail("Assistance", message, settings.EMAIL_HOST_USER, [email]) 
                messages.success(request, f'We have successfully recorded your request!')
            except BadHeaderError:
                messages.error(request,f'Something went wrong! Please Try Again')
            return redirect('assistance')
        else:
            form = AssistanceForm()
    return render(request, 'users/assistance.html', {'form': assistance_form})