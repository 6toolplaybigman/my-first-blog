from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]


#0827 작업

'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('marcador.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='mysite_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':reverse_lazy/('marcador_bookmark_list')}, name='mysite_logout'),

    url(r'^create/$', 'marcador.views.bookmark_create', name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$','marcador.views.bookmark_edit', name='marcador_bookmark_edit'),


    url(r'^user/(?P<username>[-\w]+)/$','marcador.views.bookmark_user', name='marcador_bookmark_user'),
    url(r'^$','marcador.views.bookmark_list', name='marcador_bookmark_list'),
]


'''

'''
#이건 mysite urls 이고
#이거 받은 부분

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^', include('marcador.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
'''

'''
#이건 marcador/urls.py
from django.conf.urls import url
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',name='marcador_bookmark_user'),
    url(r'^create/$', 'marcador.views.bookmark_create',name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'marcador.views.bookmark_edit', name='marcador_bookmark_edit'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
'''
