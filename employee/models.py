from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=20)
    idnumber=models.IntegerField()
    designation=models.CharField(max_length=20)
    experience=models.IntegerField()
    image=models.ImageField(upload_to="img",blank=True,null=True)

    def __str__(self):
        return self.idnumber