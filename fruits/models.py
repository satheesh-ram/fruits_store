from django.db import models

class Fruit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'fruit_images/')
    rating = models.IntegerField(default=5)

    def __str__(self):
        return str(self.id) + '-' + self.name
