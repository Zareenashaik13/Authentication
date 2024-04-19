from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Emp_Id = models.IntegerField(null=True)
    Designation = models.CharField(max_length=50,null=True)
    Location = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name