from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include
from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Instagram Clones APIS",
        default_version='v1',
        description="Instagram Clones API",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Instagram License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('user/', include('user.urls')),
                  path('post/', include('post.urls')),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
