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
	# queryset = Card.objects.all()
	serializer_class = CardSerializer
	# permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Card.objects.filter(user=self.request.user)

# class CardCreateAPIView(CreateAPIView):
# 	queryset = Card.objects.all()
# 	serializer_class = CardSerializer
# 	# permission_classes = [IsAuthenticated]

# 	def perform_create(self, serializer):
# 		serializer.save(uservendor=self.request.user)

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
	serializer_class = PointSerializer

	# def perform_create(self, serializer):
	# 	serializer.save()
	# 	card = Card.objects.get(id=serializer.data['card'])
	# 	if card.points.count()%card.vendor.points == 0:
	# 		Reward.objects.create(card=card)


class Reward(CreateAPIView):
	queryset = Reward.objects.all()
	serializer_class = RewardSerializer

class ProfileDetails(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'customer_id'

	def get_object(self):
		return self.request.user

