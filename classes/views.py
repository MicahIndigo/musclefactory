from django.shortcuts import render
from .models import GymClass


def class_list(request):
    classes = GymClass.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})
