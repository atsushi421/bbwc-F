from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Message)
class CategoryAdmin(admin.ModelAdmin):
    pass