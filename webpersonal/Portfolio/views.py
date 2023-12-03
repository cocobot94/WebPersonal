from django.shortcuts import render
from Portfolio.models import Project


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'Portfolio/portfolio.html',context)




