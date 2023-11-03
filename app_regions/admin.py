from django.contrib import admin
from .models import UzbRegions, UzbDistricts
# Register your models here.

a = [UzbRegions, UzbDistricts]
for i in a:
    admin.site.register(i)