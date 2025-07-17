from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.employee_list, name='employee_list'), 
    path('add/', views.employee_create, name='employee_add'), 
    path('edit/<int:id>/', views.employee_update, name='employee_edit'), 
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), 
]