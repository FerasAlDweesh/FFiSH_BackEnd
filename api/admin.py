from django.contrib import admin
from .models import Vendor, Card, Point, Reward

admin.site.register(Vendor)
admin.site.register(Card)
admin.site.register(Point)
admin.site.register(Reward)