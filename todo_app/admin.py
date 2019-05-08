from django.contrib import admin
from .models import School
from .models import Professor

# Register your models here.
admin.site.register(School)
admin.site.register(Professor)