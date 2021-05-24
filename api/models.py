from django.db import models

# Create your models here.

class OfficeInventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name