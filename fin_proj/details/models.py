from django.db import models


# Create your models here.
class Instrument(models.Model):
    instrument_id = models.IntegerField()
    type = models.TextField()
    diameter = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self) -> str:
        return f'{self.instrument_id} {self.type} диаметр{self.diameter}'


class ACLN(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    figure = models.ImageField(upload_to='fig/')
    instrument_id = models.ForeignKey(Instrument, on_delete=models.DO_NOTHING)
    speed =  models.IntegerField()
    rpm =   models.IntegerField()
    programm =  models.TextField()    