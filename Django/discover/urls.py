from django.conf.urls import url

from .views import UploadView, AboutView

urlpatterns = [
    url(r'^$', UploadView.as_view(), name='upload'),
    url(r'^details/', UploadView.as_view(), name='details'),
    url(r'^about/', AboutView.as_view(), name='about'),
]
