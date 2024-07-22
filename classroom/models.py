# pylint: disable=C0115,C0116

from django.db import models

class Classroom(models.Model):
    class_name = models.CharField(max_length=255, blank=True)
    class_capacity = models.SmallIntegerField(default=0)
    class_schedule = models.TextField(blank=True)
    class_attendance = models.TextField(blank=True)
    class_projects = models.TextField(blank=True)
    class_activities = models.TextField(blank=True)
    class_representatives = models.TextField(blank=True)
    class_policies = models.TextField(blank=True)
    class_requirements = models.TextField(blank=True)
    class_members_images = models.ImageField(upload_to='classroom_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.class_name} - {self.class_members_images}"