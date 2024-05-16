from django.contrib import admin
from shutterApp import models

# Register your models here.


admin.site.register(models.ShutterDtls)
admin.site.register(models.Sales_TeamClass)
admin.site.register(models.ManufacturersDtlClass)
admin.site.register(models.Customer)
admin.site.register(models.OrderItems)
admin.site.register(models.feedBack)

