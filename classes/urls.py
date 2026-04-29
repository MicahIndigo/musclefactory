from django.urls import path
from .views import class_list, book_class


urlpatterns = [
    path('', class_list, name='class_list'),
    path('book/<int:class_id>/', book_class, name='book_class'),
]
