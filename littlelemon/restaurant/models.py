from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self) -> str:
        return f"{self.first_name}"

class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_item_descprtion = models.TextField(max_length=1000, default='')

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
