from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True, upload_to='vendor_images')
	points = models.PositiveIntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uservendor')

	def __str__(self):
		return self.name

class Card(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercard')
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendors')

	def __str__(self):
		return "%s %s" % (self.vendor, self.user.username)

class Point(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='points')

	def __str__(self):
		return "%s %s" % (self.card.vendor, self.card.user.username)
	
class Reward(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='cardreward')


# class RedeemedReward(models.Model):
#...future