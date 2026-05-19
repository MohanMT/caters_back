from django.urls import path
from .views import caterers, caterer_detail

urlpatterns = [
    path('caterers/', caterers),
    path('caterers/<str:id>/', caterer_detail),
]