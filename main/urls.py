from django.contrib import admin
from django.urls import path, include
from djangorest import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('modelview', views.Model_View_Set, basename='modelviewuser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('home/', views.home),
]
