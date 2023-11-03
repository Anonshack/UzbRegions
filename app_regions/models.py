from django.db import models


# Create your models here.
class UzbRegions(models.Model):
    region_name_uz = models.CharField(max_length=50)
    region_name_en = models.CharField(max_length=50)
    region_name_ru = models.CharField(max_length=50)

    class Meta:
        db_table = 'uzb_regions'


class UzbDistricts(models.Model):
    district_name_uz = models.CharField(max_length=50)
    district_name_en = models.CharField(max_length=50)
    district_name_ru = models.CharField(max_length=50)
    district_region = models.ForeignKey(UzbRegions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'uzb_dictricts'