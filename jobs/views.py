from django.shortcuts import render
from jobs.models import Job

# Create your views here.
def home(request):
    # To get all objects of job and convert them into dictionary
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})