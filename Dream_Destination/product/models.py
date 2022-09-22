from django.db import models


class TravellPlace(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pics")
    des=models.TextField()
    cost=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class comments(models.Models):
    place=models.ForeignKey(TravellPlace,related_name="commands",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    cmt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)         
    
