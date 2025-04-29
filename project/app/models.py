from django.db import models

# Create your models here.

class Fitness(models.Model):
    Student_name=models.CharField(max_length=50)
    Student_email=models.EmailField()
    Student_contact=models.IntegerField()
    
    Student_age=models.IntegerField()
    Student_plan=models.CharField(max_length=40)
    Student_Gender=models.CharField(max_length=50)
    Student_file=models.ImageField(upload_to='image/')
    # Student_Image=models.ImageField(upload_to='image/')
    # Student_Resume=models.FileField(upload_to='file/')
    Student_Password=models.CharField(max_length=50)
    Student_message=models.CharField(max_length=211)
