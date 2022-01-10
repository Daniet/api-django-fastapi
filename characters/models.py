from django.db import models

# Create your models here.

class Character(models.Model):

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
 