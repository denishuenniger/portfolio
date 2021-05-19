from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("", views.home, name="home"),
]
