from django.db import models


class TravellPlace(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pics")
    des=models.TextField()
    cost=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    
