from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    code = models.PositiveSmallIntegerField(default=0) 
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    hire_date = models.DateField()
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    picture = models.ImageField(upload_to='teacher_pics/', blank=True, null=True)
    course_code = models.SmallIntegerField(default=0)
    salary = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"