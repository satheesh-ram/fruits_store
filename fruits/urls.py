from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fruits.index'),
    path('<int:id>/', views.show, name='fruits.show'),
]