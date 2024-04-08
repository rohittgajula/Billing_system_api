from django.urls import path
from . import views


urlpatterns = [
    path('employee/register/', views.create_employee, name='create-employee'),
    path('all-employees/', views.all_employees, name='all-employees'),
]

