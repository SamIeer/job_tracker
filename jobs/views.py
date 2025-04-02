from django.shortcuts import render, redirect
from jobs.models import JobApplications             
from jobs.forms import JobApplicationForm  # Fixed import

# Create your views here.
def home(request):
    jobs = JobApplications.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = JobApplicationForm()
    return render(request, 'add_job.html', {'form': form})

