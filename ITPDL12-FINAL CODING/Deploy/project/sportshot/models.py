from django.db import models

class UserSportsModel(models.Model):
    image = models.ImageField(upload_to = 'sport/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)