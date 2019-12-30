from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
CardList,
VendorList,
VendorCreate,
Point,
CreatePoint,
Reward,
ProfileDetails,
DashboardList,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
  
    path('cards/', CardList.as_view(), name='card-list'),
    path('vendors/', VendorList.as_view(), name='vendor-list'),

    path('vendors/create/', VendorCreate.as_view(), name='vendor-create'),
    path('vendors/dashboard/', DashboardList.as_view(), name='vendor-dashboard'),

    path('points/', Point.as_view(), name='points'),
    path('createpoint/', CreatePoint.as_view(), name='pointcreate'),

    path('Rewards/', Reward.as_view(), name='rewards'),

    path('profile/', ProfileDetails.as_view(), name="profile"),
]