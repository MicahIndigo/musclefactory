from django.urls import path
from .views import class_list, book_class, my_bookings


urlpatterns = [
    path('', class_list, name='class_list'),
    path('book/<int:class_id>/', book_class, name='book_class'),
    path('my-bookings/', my_bookings, name='my_bookings'),
]
