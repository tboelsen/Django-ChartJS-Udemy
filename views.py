from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

def HomeView(request):
    return render(request, 'home.html', {})

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles.html'
