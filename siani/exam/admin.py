from django.contrib import admin

# Register your models here.
from .models import Stage

@admin.register(Stage)
class StageAdmoin(admin.ModelAdmin):
    list_display =['stage','month','year']