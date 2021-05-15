from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    path("", views.home, name="home"),
    path("curriculum/", views.curriculum, name="curriculum")
]
