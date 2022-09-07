from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='StaffView'),
    path('show/', views.staff_show, name='StaffShow'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]