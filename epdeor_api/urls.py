"""
URL configuration for epdeor_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def options_view(request):
    response = JsonResponse({'detail': 'OK'})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

schema_view = get_schema_view(
    openapi.Info(
            title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("options/", csrf_exempt(options_view)),
    path('api-usuarios/', include('apis.usuarios.urls')),
    path('api-notificaciones/', include('apis.notificaciones.urls')),
    path('api-almacenes/', include('apis.almacenes.urls')),
    path('api-materiales/', include('apis.material.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
