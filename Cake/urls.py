from django.conf import settings
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include("django.conf.urls.i18n")),
    path('', include('final_project.urls')),

    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)