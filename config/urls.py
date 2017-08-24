from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:

    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={
            'exception': Exception('Bad Request!')}),

        url(r'^403/$', default_views.permission_denied, kwargs={
            'exception': Exception('Permission Denied')}),

        url(r'^404/$', default_views.page_not_found, kwargs={
            'exception': Exception('Page not Found')}),

        url(r'^500/$', default_views.server_error),
    ]
