from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
]