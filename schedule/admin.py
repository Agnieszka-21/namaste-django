from django.contrib import admin
from .models import YogaStyle, StyleDescription, GroupClass

# Register your models here.
admin.site.register(YogaStyle)
admin.site.register(StyleDescription)
admin.site.register(GroupClass)

