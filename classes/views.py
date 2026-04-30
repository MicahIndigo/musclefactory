from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GymClass, Booking
from profiles.models import Profile


@login_required
def class_list(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if not profile.is_member:
        messages.error(request, "You must purchase a membership to access classes.")
        return redirect('/checkout/buy/')
    
    classes = GymClass.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})


@login_required
def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    profile = Profile.objects.get(user=request.user)

    # Only members can book
    if not profile.is_member:
        messages.error(request, "You must purchase a membership to view classes.")
        return redirect('/checkout/buy/')

    # prevent duplicate bookings
    if Booking.objects.filter(user=request.user, gym_class=gym_class).exists():
        return redirect('class_list')

    Booking.objects.create(user=request.user, gym_class=gym_class)
    
    messages.success(request, f"You have successfully booked {gym_class.name}!")
    return redirect('class_list')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'classes/my_bookings.html', {'bookings': bookings})
