from django.urls import path
from . import views

urlpatterns = [
    path('lookup/', views.lookup, name="lookup"),
]
