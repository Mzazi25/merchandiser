from django.urls import path,include
from . import views

urlpatterns = [
    path('api/merchandiser/', views.MerchandiserList.as_view()),
    path('api/manager/', views.ManagerList.as_view()),
    path('api/routes/', views.RouteList.as_view()),
]