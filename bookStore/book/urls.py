from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'books',views.home, basename='home')

urlpatterns = [
    path('', include(router.urls)),
]
