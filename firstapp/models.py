from django.db import models

# Create your models here.


class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class contact(models.Model):
    emailf=models.EmailField()
    contact=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.emailf
