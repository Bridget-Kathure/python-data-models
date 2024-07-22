# pylint: disable=C0115,C0116

from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length=255, blank=True)
    course_description = models.TextField(blank=True)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    code = models.SmallIntegerField(default=0)
    grading_system = models.CharField(max_length=100, blank=True)
    course_materials = models.TextField(blank=True)
    course_fee = models.SmallIntegerField(default=0)
    course_outline = models.TextField(blank=True)
    course_language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.course_title} - {self.course_description}"