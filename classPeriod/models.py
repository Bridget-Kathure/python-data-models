# pylint: disable=C0115,C0116


from django.db import models
from django.db.models.manager import BaseManager
from course.models import Course

class ClassPeriod(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    day_of_week = models.CharField(max_length=20, blank=True)
    objects: BaseManager["ClassPeriod"]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.day_of_week} ({self.start_time} - {self.end_time})"