from django.db import models

class Resume(models.Model):
    photo = models.ImageField(upload_to='photos/')
    about_me = models.TextField()
    education = models.TextField()
    education_files = models.FileField(upload_to='education_files/', blank=True, null=True)
    work_experience = models.TextField()
    desired_position = models.CharField(max_length=100)
    additional_info = models.TextField()
    contacts = models.TextField()