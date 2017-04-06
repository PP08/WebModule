from django.db import models

# Create your models here.
class Document_Single(models.Model):
    single = models.FileField(upload_to='documents/single/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Document_Multiple(models.Model):
    multiple = models.FileField(upload_to='documents/multiple/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Table_single(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    spl_value = models.FloatField()
    measured_at = models.DateTimeField()

    class Meta:
        db_table = "single_measurement"