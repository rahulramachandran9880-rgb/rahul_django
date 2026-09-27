from django.contrib import admin
from . models import MovieInfo, Director,Actor,CensorInfo

# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(CensorInfo)
