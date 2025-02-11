from django.contrib import admin
from .models import ModelView

# Register your models here.
@admin.register(ModelView)
class ModelViewAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'phone', 'address']