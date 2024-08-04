from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'books',views.home, basename='home')
router.register(r'register-user',views.register_user, basename='register_user')
router.register(r'book-by-country/<int:pk>',views.book_by_country, basename='book_by_country')
urlpatterns = [
    path('', include(router.urls)),
]
