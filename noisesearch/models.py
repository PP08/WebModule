from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

'''files'''


class PrivateFilesSingle(models.Model):
    file = models.FileField(upload_to='documents/private/single')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Private_single_files"


class PublicFilesSingle(models.Model):
    file = models.FileField(upload_to='documents/public/single')
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Public_single_files"

class PrivateFilesMultiple(models.Model):
    file = models.FileField(upload_to='documents/private/multiple')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Private_multiple_files"

class PublicFilesMultiple(models.Model):
    file = models.FileField(upload_to='documents/public/multiple')
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Public_multiple_files"

'''tables'''

'''single'''


class PrivateSingleAverage(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    average_spl = models.FloatField()
    duration = models.DurationField(default=0)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "Private_single_average"


class PrivateSingleDetail(models.Model):
    id = models.AutoField(primary_key=True)
    measurement_id = models.ForeignKey(PrivateSingleAverage, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spl_value = models.FloatField()
    measured_at = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.measured_at)

    class Meta:
        db_table = "Private_single_detail"


class PublicSingleAverage(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    average_spl = models.FloatField()
    duration = models.DurationField(default=0)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.duration)

    class Meta:
        db_table = "Public_single_average"


class PublicSingleDetail(models.Model):
    id = models.AutoField(primary_key=True)
    measurement_id = models.ForeignKey(PublicSingleAverage, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spl_value = models.FloatField()
    measured_at = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.measured_at)

    class Meta:
        db_table = "Public_single_detail"


# class Sum_measurement_single(models.Model):
#     measurement_id = models.AutoField(primary_key=True)
#     device_id = models.CharField(max_length=30)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     average_spl_value = models.FloatField()
#     measurement_duration = models.DurationField(default=0)
#     start_time = models.DateTimeField(default=None)
#     end_time = models.DateTimeField(default=None)
#
#     def __str__(self):
#         return str(self.measurement_duration)
#
#     class Meta:
#         db_table = "average_single"

'''multiple'''


class PrivateMultipleAverage(models.Model):
    """"""
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=30)
    start_point = JSONField()
    end_point = JSONField()
    average_spl = models.FloatField()
    distance = models.FloatField()
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name + '  distance: ' + str(self.distance) + ' meters'

    class Meta:
        db_table = "Private_multiple_average"


class PrivateMultipleDetail(models.Model):
    """"""
    id = models.AutoField(primary_key=True)
    measurement_id = models.ForeignKey(PrivateMultipleAverage, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spl_value = models.FloatField()
    measured_at = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.measured_at)

    class Meta:
        db_table = "Private_multiple_detail"

class PublicMultipleAverage(models.Model):
    """"""
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=30)
    start_point = JSONField
    end_point = JSONField
    average_spl = models.FloatField()
    distance = models.FloatField()
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.distance)

    class Meta:
        db_table = "Public_multiple_average"

class PublicMultipleDetail(models.Model):
    """"""
    id = models.AutoField(primary_key=True)
    measurement_id = models.ForeignKey(PublicMultipleAverage, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spl_value = models.FloatField()
    measured_at = models.DateTimeField(default=None)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.measured_at)

    class Meta:
        db_table = "Public_multiple_detail"
# class Table_single(models.Model):
#     id = models.AutoField(primary_key=True)
#     measurement_id = models.ForeignKey(Sum_measurement_single, on_delete=models.CASCADE)
#     device_id = models.CharField(max_length=30)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     spl_value = models.FloatField()
#     measured_at = models.DateTimeField(default=None)
#
#     def __str__(self):
#         return str(self.measured_at)
#
#     class Meta:
#         db_table = "single_measurement"
