from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'peapron.views.home', name='home'),
    # url(r'^peapron/', include('peapron.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    'peapron.views',
    url(r'^$', 'index', name="index"),
    url(r'^login/', 'login', name="login"),
    url(r'^user_regist/', 'user_regist', name="user_regist"),
)


