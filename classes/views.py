from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GymClass, Booking


def class_list(request):
    classes = GymClass.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})


@login_required
def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    # prevent duplicate bookings
    if Booking.objects.filter(user=request.user, gym_class=gym_class).exists():
        return redirect('class_list')

    Booking.objects.create(user=request.user, gym_class=gym_class)

    return redirect('class_list')
