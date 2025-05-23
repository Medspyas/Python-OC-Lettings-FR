from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from oc_lettings_site import views as core_view

urlpatterns = [
    path("", core_view.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
    path('test500', core_view.test_500),
    path("sentry-error/", core_view.test_error),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)