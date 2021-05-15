from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class events(models.Model):
    starttime = models.TimeField()
    endtime = models.TimeField()
    name = models.TextField(max_length=24)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = 1,null=True)
