from django.db import models

# Create your models here.


class Rain(models.Model):
    """
    Stores rain mm in one date and ground.
    """

    rain_date = models.DateField(help_text="Rain Date")
    rainfall = models.PositiveIntegerField(help_text="Rain Fall (mm)")
    ground = models.ForeignKey(
        'Ground', on_delete=models.CASCADE, help_text="Related Ground")

    def __str__(self):
        return "{} / {} - {}".format(
                str(self.ground), 
                str(self.rain_date), 
                str(self.rainfall)
        )


class Ground(models.Model):

    """
    Stores ground data like position and area.
    """

    name = models.fields.CharField(max_length=50, unique=True)
    lat = models.fields.FloatField()
    lon = models.fields.FloatField()
    hectare = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
