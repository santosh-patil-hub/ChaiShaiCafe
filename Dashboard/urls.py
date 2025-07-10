from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard/admin/', views.Dashboard,name='dashboard_admin'),

]
