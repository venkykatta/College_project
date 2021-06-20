from django.db import models


class managerModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='managerregister'


class uploadmodel(models.Model):
    filename = models.CharField(max_length=100)
    filetype = models.CharField(max_length=100)
    #description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename














