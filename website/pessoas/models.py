from django.db import models

GENDERS = (
    ('M', "Male"),
    ('F', "Female"),
    ('R', "Rather not say"),
)

# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDERS, default='R', max_length=10)
    age = models.IntegerField()


    class Meta:
        ordering = ('id',)