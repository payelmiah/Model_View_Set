from django.shortcuts import render
from .models import ModelView
from .serializers import ModelViewSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class Model_View_Set(viewsets.ModelViewSet):
    queryset = ModelView.objects.all()
    serializer_class = ModelViewSerializer
    permission_classes = [IsAuthenticated]

def home(request):
    users = ModelView.objects.all()
    return render(request, 'base.html', {'users': users})