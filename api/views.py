from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Card, Vendor, Point, Reward
from .serializers import UserCreateSerializer, CardSerializer, VendorSerializer, VendorCreateSerializer, PointSerializer, RewardSerializer, ProfileSerializer, DashboardSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CardList(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.usercard

class VendorList(ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated]


class VendorCreate(CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorCreateSerializer
     
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreatePoint(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        vendor_obj = Vendor.objects.get(id=request.data.get('vendor'))
        card_obj, created = Card.objects.get_or_create(user=request.user, vendor=vendor_obj)
        point_obj = Point.objects.create(card=card_obj)
        return Response(status=status.HTTP_201_CREATED)


class Reward(CreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class DashboardList(ListAPIView):
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return self.request.user.uservendor.vendors



class ProfileDetails(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'customer_id'

    def get_object(self):
        return self.request.user

