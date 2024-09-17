from django.contrib import admin
from .models import YogaStyle, StyleDescription, GroupClass, Booking, SpecificGroupClass

# Register your models here.
admin.site.register(YogaStyle)
admin.site.register(StyleDescription)
admin.site.register(GroupClass)
admin.site.register(Booking)
admin.site.register(SpecificGroupClass)

