from django.db import models

# Create your models here.

class Contact(models.Model):
    msg_id = models.CharField(max_length=70, default="")
    name = models.TextField(max_length=50)
    email = models.CharField(max_length=70, default="")
    desc = models.TextField(max_length=500, default="")


    def __str__(self):
        return self.name
