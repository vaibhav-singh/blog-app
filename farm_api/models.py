from django.contrib.gis.db import models

# Create your models here.

class Villages(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coo = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.coo.x, self.coo.y)
