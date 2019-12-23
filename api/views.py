from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Card, Vendor, Point, Reward
from .serializers import UserCreateSerializer, CardSerializer, VendorSerializer, VendorCreateSerializer, PointSerializer, RewardSerializer, ProfileSerializer
# from .permissions import IsOrderOwner

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CardList(ListAPIView):
	queryset = Card.objects.all()
	serializer_class = CardSerializer
	# permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(customer=self.request.user)

class VendorList(ListAPIView):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer
	permission_classes = [IsAuthenticated]

class VendorCreate(CreateAPIView):
	serializer_class = VendorCreateSerializer
	
class PointList(ListAPIView):
	queryset = Point.objects.all()
	serializer_class = PointSerializer

class RewardList(ListAPIView):
	queryset = Reward.objects.all()
	serializer_class = RewardSerializer

class ProfileDetails(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'customer_id'

	def get_object(self):
		return self.request.user

