from django.db import models


class Course(models.Model):
    course_title = models.TextField()
    course_description = models.TextField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    code = models.SmallIntegerField()
    grading_system = models.TextField()
    course_materials = models.TextField()
    course_fee = models.SmallIntegerField()
    course_outline = models.TextField()
    course_language = models.TextField()

    def __str__(self):
        return f"{self.course_title}  {self.course_description}"
# Create your models here.
