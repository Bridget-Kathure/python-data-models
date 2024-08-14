# pylint: disable=C0115 , C0116

from django.db import models

import course

class Student(models.Model):
    courses = models.ManyToManyField(course)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    code = models.PositiveSmallIntegerField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    age = models.SmallIntegerField(default=0)
    phonenumber = models.CharField(max_length=20, blank=True)
    immediate_contact = models.CharField(max_length=20, blank=True)
    class_code = models.SmallIntegerField(default=0)
    course_code = models.SmallIntegerField(default=0)
    pic = models.ImageField(upload_to='student_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"