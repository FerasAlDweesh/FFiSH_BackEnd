from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .models import Card, Vendor, Point, Reward
from .serializers import UserCreateSerializer, CardSerializer, VendorSerializer, VendorCreateSerializer, PointSerializer, RewardSerializer, ProfileSerializer, DashboardSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CardList(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     cards = Card.objects.get(request.user)
    #     serializer = CardSerializer(cards, many=True)
    #     return Response(serializer.data)

# class CardCreateAPIView(CreateAPIView):
#   queryset = Card.objects.all()
#   serializer_class = CardSerializer
#   # permission_classes = [IsAuthenticated]

#   def perform_create(self, serializer):
#       serializer.save(uservendor=self.request.user)

class VendorList(ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated]


class VendorCreate(CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorCreateSerializer

     
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class Point(CreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class CreatePoint(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        card_obj, created = Card.objects.get_or_create(user=request.user, vendor=request.data.get("vendor"))
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

