from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile
from django.core.files.base import ContentFile
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class UserProfile(View):
    template_name = 'profile.html'

    def get(self, request):
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None
        form_data = {
            'name': user_profile.full_name if user_profile else '',
            'email': request.user.email if user_profile else '',
            'designation': user_profile.designation if user_profile else '',
            'mobile_no': user_profile.mobile_number if user_profile else '',
            'profile_image': user_profile.profile_image if user_profile else '',
            'profile_summary': user_profile.profile_summary if user_profile else '',
            'city': user_profile.city if user_profile else '',
            'state': user_profile.state if user_profile else '',
            'country': user_profile.country if user_profile else '',
        }
        context = {
            'profile': user_profile,
            'form_data': form_data
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None
        uploaded_image = request.FILES.get('profile_image', None)
        if uploaded_image:
            user_profile.profile_image.save(uploaded_image.name, ContentFile(uploaded_image.read()))
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        mobile_number = request.POST.get('mobile_no')
        profile_summary = request.POST.get('profile_summary')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        if user_profile:
            user_profile.full_name = full_name
            user_profile.designation = designation
            user_profile.mobile_number = mobile_number
            user_profile.profile_summary = profile_summary
            user_profile.city = city
            user_profile.state = state
            user_profile.country = country
            user_profile.save()

            user_profile.user.email = email
            user_profile.user.save()

        return redirect('user-profile')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, "about.html")

