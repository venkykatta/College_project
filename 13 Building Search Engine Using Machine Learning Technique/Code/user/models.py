from django.db import models


class userModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userregister'


class weightmodel(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    weight=models.CharField(max_length=100)
    rank=models.CharField(max_length=100,default="", editable=False)
    label=models.CharField(max_length=100,default="", editable=False)

    def __str__(self):
        return self.filename
    class Meta:
        db_table='weight'

