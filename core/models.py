from django.db import models

# Create your models here.


class GenCode(models.Model):
    # Saves the code into our database for further verification.
    code = models.CharField(max_length=200)
    generatedby = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    def __str__(self):
        return self.generatedby

class QrCode(models.Model):
    code = models.CharField(max_length=200, null=True)
    fullname = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    def __str__(self):
        return self.location

