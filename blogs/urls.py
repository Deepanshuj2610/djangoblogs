from django.urls import path
from . import views

app = "blogs"

urlpatterns = [
    path('', views.home ,name='home'),
]