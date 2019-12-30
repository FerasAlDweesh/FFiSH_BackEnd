from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Card, Vendor, Point, Reward


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'id']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'image', 'points', 'id']

class CardSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    user = serializers.SerializerMethodField()
    # points = serializers.SerializerMethodField()
    class Meta:
        model = Card
        fields = [ 'vendor', 'id', 'user']

    def get(self, request):
        cards = Card.objects.get(request.user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def get_user(self, obj):
        return "%s %s" % (obj.user.first_name, obj.user.last_name)

    # def get_queryset(self):
    #     user = self.request.user
    #     return user.card.all()

        # def get_points(self, obj):
        #     return obj.points % obj.vendor.points 

class VendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'image', 'points',]

# Point Create:
class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['card']

class DashboardSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    points = serializers.SerializerMethodField()
    class Meta:
        model = Card
        fields = ['id', 'user', 'points' ]

    def get_points(self, obj):
        return obj.points.count()


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['status', 'date', 'card', 'id']

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'name', 'email']

    def get_name(self, obj):
        return "%s %s"%(obj.first_name, obj.last_name)

    

