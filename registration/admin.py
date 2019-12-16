from django.contrib import admin

# Register your models here.
from .models import IITJUser,Project,Feedback,IssueMaterial,MustKnowPeople

class IITJUserAdmin(admin.ModelAdmin):
	pass 

admin.site.register(IITJUser,IITJUserAdmin)
admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(IssueMaterial)
admin.site.register(MustKnowPeople)