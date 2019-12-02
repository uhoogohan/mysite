from django.db import models

class Meibo(models.Model):
    simei = models.CharField(max_length=50)
    simei_kana= models.CharField(max_length=50)
    email_addr = models.CharField(max_length=50)
    seibetu = models.CharField(max_length=10)
    tanjo_bi = models.DateField()
    blood_gata = models.CharField(max_length=5)
    chiiki = models.CharField(max_length=50)
    phone_bango = models.CharField(max_length=10)

    def __str__(self):
        return self.simei
