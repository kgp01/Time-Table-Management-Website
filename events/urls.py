
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("addevent", views.addevent, name="addevent"),
    path("showtimetable",views.showtimetable, name="showtimetable"),
    path("deleteone/<int:cid>",views.deleteone,name="deleteone"),
    path("deleteall", views.deleteall,name = "deleteall"),
    ]
