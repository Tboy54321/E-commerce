from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Companies

admin.site.register(Companies)
# admin.site.register(User, UserAdmin)