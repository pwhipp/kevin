from django.conf.urls import patterns, include, url
from django.contrib import admin
from step_game.views import MainView, ResultView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^result/(\w*)/(\w*)/', ResultView.as_view(), name='result'),
    url(r'^admin/', include(admin.site.urls)),)
