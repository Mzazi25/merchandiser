from django.urls import path
from route.views import CustomAuthToken, ManagerOnlyView, ManagerSignupView, MerchandiserOnlyView,MerchandiserSignupView,LogoutView

app_name = 'route'
urlpatterns = [
    path('signup/manager/',ManagerSignupView.as_view()),
    path('signup/merchandiser/',MerchandiserSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(),name='auth-token'),
    path('logout/',LogoutView.as_view(),name='logout=view'),
    path('manager/dashboard/',ManagerOnlyView.as_view(),name='manager-dashboard'),
    path('merchandiser/dashboard/',MerchandiserOnlyView.as_view(),name='merchandiser-dashboard'),
]