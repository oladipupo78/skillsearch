from django.contrib import admin
from .models import Course,Enrolled,VideoRepo,Review

admin.site.register(Course)
admin.site.register(Enrolled)
admin.site.register(VideoRepo)
admin.site.register(Review)

