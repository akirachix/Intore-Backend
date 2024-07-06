from django.db import models

# Create your models here.
class Recycler(models.Model):
    
 recycler_id = models.PositiveSmallIntegerField()
 recyler_name = models.CharField(max_length=20)
 recycler_email = models.EmailField(max_length=20)
 password = models.CharField(max_length=20)
 phone_number = models.CharField(max_length=20)
 business_name = models.CharField(max_length=20)
 mode_of_payment = models.CharField(max_length=20)
 
 def __str__(self):
  return f"{self.recycler_id} {self.recyler_name}"
