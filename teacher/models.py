from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField() 
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length= 30)
    bio = models.TextField()
    qualifications = models.TextField()
    hire_date = models.DateField()
    gender = models.TextField()
    picture = models.ImageField()
    course_code = models.SmallIntegerField()
    salary = models.BigIntegerField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
# Create your models here.
