<<<<<<< HEAD
from django.urls import path

urlpatterns = [
]
=======
from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.signin),
]
>>>>>>> 9c55c653ed5cd63d594184549c1c3dccc21b43cc
