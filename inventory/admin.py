from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Subcategories)
admin.site.register(Inventory)
admin.site.register(Gallery)
admin.site.register(Consecutive)
admin.site.register(Order)
admin.site.register(PaymentForm)