from django.contrib import admin

# Register your models here.
# 
from .models import Cliente
from .models import Cobro

admin.site.register(Cliente)
admin.site.register(Cobro)