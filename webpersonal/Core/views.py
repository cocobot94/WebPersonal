from django.shortcuts import render
from Core.models import Acerca, Yo, Info


# Create your views here.
def portada(request):
    context = {}
    return render(request, "Core/portada.html", context)


def about(request):
    yo = Yo.objects.all()
    items = Acerca.objects.all()
    context = {"items": items, "yo": yo}
    return render(request, "Core/about.html", context)


def conatct(request):
    information = Info.objects.all()
    context = {"information": information}
    return render(request, "Core/contact.html", context)
