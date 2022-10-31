from django.shortcuts import render
from .models import Jobs


# Create your views here.
def jobs(request):
  jobs = Jobs.objects.all()
  context = {
    'jobs': jobs,
  }
  return render(request, 'jobs.html', context=context)
