from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    # General urls
    path('', views.Employees.as_view()),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    # Viewset Url
    # path('', include(router.urls)),

]
