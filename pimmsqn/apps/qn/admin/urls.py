from django.conf.urls.defaults import *

# Enabling the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/qn/component/copy/$', 'cmip5q.qn.admin.admin_views.modelcopy'),
)
