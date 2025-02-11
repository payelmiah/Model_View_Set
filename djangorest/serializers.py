
from rest_framework import serializers
from .models import ModelView

class ModelViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelView
        fields = ['id', 'name', 'age', 'Bio', 'email', 'phone', 'address']