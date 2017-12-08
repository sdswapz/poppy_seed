from django.conf.urls import url
from .views import IndexView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<name>\w+)/$', DetailView.as_view(), name='detail'),
]
