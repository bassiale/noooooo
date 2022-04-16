from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("live_data", views.live_data, name='live_data'),
    path("no/<int:temperature>/<int:pressure>/<int:altitude>", views.no, name='no'),
]