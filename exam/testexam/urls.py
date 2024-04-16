from django.urls import path
from . import views

urlpatterns = [
    path('', views.testform, name="testform"),
    path('deltestform/<pk>/', views.deltestform, name="deltestform"),
    path('search/', views.search, name="search"),

]