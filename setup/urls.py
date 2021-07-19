from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, authentication
from aluraflix.views import ProgramaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix",
      default_version='v1',
      description="Provedor local de séries e filmes desenvolvida pela Alura no curso de Django REST",
      terms_of_service="#",
      contact=openapi.Contact(email="c3po@alura.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.IsAdminUser,),
   authentication_classes=(authentication.BasicAuthentication,),
)

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
