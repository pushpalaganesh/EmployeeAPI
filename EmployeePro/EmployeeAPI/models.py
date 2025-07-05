from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=30)
    emp_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.emp_name
