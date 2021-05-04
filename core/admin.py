from django.contrib import admin

from .models import GenCode
from .models import QrCode

# Register your models here.
admin.site.register(GenCode)
admin.site.register(QrCode)
