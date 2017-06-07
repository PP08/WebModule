from django.contrib import admin
from .models import PublicSingleDetail, PublicSingleAverage, PublicMultipleDetail, PublicMultipleAverage
# Register your models here.

admin.site.register(PublicSingleDetail)
admin.site.register(PublicSingleAverage)
admin.site.register(PublicMultipleDetail)
admin.site.register(PublicMultipleAverage)