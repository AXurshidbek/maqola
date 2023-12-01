from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Muallif(models.Model):
    ism=models.CharField(max_length=31)
    yosh=models.PositiveSmallIntegerField()
    kasb=models.CharField(max_length=31)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha=models.CharField(max_length=55)
    sana=models.DateField()
    mavzu=models.CharField(max_length=35)
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha