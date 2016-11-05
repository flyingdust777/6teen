from django.contrib import admin

# Register your models here.
from .models import extendedUser, business, ratings

# admin.site.register(ratings)
admin.site.register(extendedUser)
admin.site.register(business)
