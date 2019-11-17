from django.contrib import admin

# Register your models here.
from .models import Students, ResultCard, Profile
admin.site.register(Students)
admin.site.register(ResultCard)
admin.site.register(Profile)
