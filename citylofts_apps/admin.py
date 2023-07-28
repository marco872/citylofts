from django.contrib import admin

# Register your models here.
# admin.py
from .models import LoftRentals, TemporaryStandRental, CoMinimizing, MaintenanceAndHousekeeping, LoftFeature, ConnectedAppliance

# Register LoftRentals model
admin.site.register(LoftRentals)

# Register TemporaryStandRental model
admin.site.register(TemporaryStandRental)

# Register CoMinimizing model
admin.site.register(CoMinimizing)

# Register MaintenanceAndHousekeeping model
admin.site.register(MaintenanceAndHousekeeping)

# Register LoftFeature model
admin.site.register(LoftFeature)

# Register ConnectedAppliance model
admin.site.register(ConnectedAppliance)
