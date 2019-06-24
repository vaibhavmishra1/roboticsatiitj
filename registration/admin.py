from django.contrib import admin

# Register your models here.
from .models import IITJUser

class IITJUserAdmin(admin.ModelAdmin):
	pass 

admin.site.register(IITJUser,IITJUserAdmin)