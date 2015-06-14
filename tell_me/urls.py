from django.conf.urls import include, url, patterns

from . import views

urlpatterns = patterns(
	'tell_me.views',
    # Examples:
    # url(r'^$', 'Fandeavor_challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.tell_me_page, name='tell_me_page'),
    url(r'^run_search/$', 'run_search')
)