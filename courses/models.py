from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg')
    name = models.CharField(max_length=30, null=True)
    field = models.CharField(max_length=30, null=True)
    topic = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=300, null=True)
    ToBeLearned = models.CharField(max_length=300, null=True)
    requirements = models.CharField(max_length=300, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    level = models.CharField(max_length=30, null=True)


class Enrolled(models.Model):
    enrollee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, default=1)


class Review(models.Model):
    review = models.CharField(max_length=100)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1,related_name='user_reviewed')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, default=1)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1,related_name='instructor_reviewed')


class VideoRepo(models.Model):
    videoname = models.CharField(max_length=100)
    videosrc = models.FileField(upload_to='videos/', blank=True,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, default=1)