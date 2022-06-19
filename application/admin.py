from django.contrib import admin
from application.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Order)