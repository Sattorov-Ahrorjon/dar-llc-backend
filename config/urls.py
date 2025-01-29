from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = "Dar LCC Dashboard"
admin.site.site_title = "Dar LCC Dashboard"
admin.site.index_title = "Welcome to Dar LCC Dashboard"

schema_view = get_schema_view(
    openapi.Info(
        title="Dar LCC Dashboard",
        default_version='v1',
        description="API for Dar LCC Dashboard",
        terms_of_service="",
        contact=openapi.Contact(email="sattorov.ahu@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger',
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    )
]

if settings.SHOW_SWAGGER:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
