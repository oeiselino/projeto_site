from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core.views import HomeView, ContatoView, ContatoEnviado

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'selariasutile.views.home', name='home'),
    # url(r'^selariasutile/', include('selariasutile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r'^eventos/', include("eventos.urls")),
    url(r'^galeria/', include("galeria.urls")),
    url(r'^produtos/', include("produtos.urls")),
    url(r'^empresa/', include("empresa.urls")),
    url(r"^contato/$", ContatoView.as_view(), name="contato"),
    url(r"^contato/enviado/$", ContatoEnviado.as_view(), name="contatoenviado"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
