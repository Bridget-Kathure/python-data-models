from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField() 
    date_of_birth = models.DateField()
    country = models.CharField(max_length= 20)
    bio = models.TextField()
    age = models.SmallIntegerField()
    phonenumber = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    immediate_contact = models.CharField(max_length=20)
    class_code = models.SmallIntegerField()
    course_code = models.SmallIntegerField()
    pic = models.ImageField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
