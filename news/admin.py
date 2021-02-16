from django.contrib import admin

# Register your models here.
from .models import Film, Regista

# documentazione: https://docs.djangoproject.com/en/2.0/ref/contrib/admin/


admin.site.register(Film)
admin.site.register(Regista)
