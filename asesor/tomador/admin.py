from django.contrib import admin

# Register your models here.

from .models import  AIO, SIF, NTC, PRO, TRD, GER



admin.site.register(AIO)
admin.site.register(SIF)
admin.site.register(NTC)
admin.site.register(PRO)
admin.site.register(TRD)
admin.site.register(GER)


