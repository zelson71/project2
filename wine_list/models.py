from django.db import models

# Create your models here.
class AllWines(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True,primary_key=True)  # Field name made lowercase.
    alcohol = models.FloatField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    subregion = models.TextField(blank=True, null=True)
    subsubregion = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    varietal = models.TextField(blank=True, null=True)
    vintage = models.FloatField(blank=True, null=True)
    winery = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_wines'

        def __str__(self):
            return self.winery
