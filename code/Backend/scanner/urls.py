from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # /scanner
    # url(r'^$', views.home, name='home'),

    # /scanner/results
    # url(r'^$', views.scan, name='welcome'),
    url(r'^results/logs$', views.FetchLog.as_view(), name='fetch_log'),
    url(r'^scan$', views.scan, name='scan'),
    url(r'^results/temp$', views.FetchList.as_view(), name='fetch_result'),
    url(r'^display/ip$', views.displayip, name='display_result_ip'),
    url(r'^display/port$', views.displayport, name='display_result_port'),
    url(r'^display/time$', views.FetchTime.as_view(), name='fetch_time'),
    url(r'^display/frequency$', views.FetchFrequency.as_view(), name='fetch_frequency'),
    url(r'^display/bandwidth$', views.FetchBandwidth.as_view(), name='fetch_bandwidth'),
    #url(r'^stop/$',views.stop,name='stop')
]

urlpatterns = format_suffix_patterns(urlpatterns)