from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = patterns('',
                      url(r'^$', 'project.views.all_projects'),
                      url(r'^(?P<project_id>\d+)/$', 'project.views.project'),
                      url(r'^api/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
                      )

urlpatterns = format_suffix_patterns(urlpatterns)