from django.conf.urls import url

from ..apis import HostingList, HostingDetail, PhotoList, PhotoDetail

urlpatterns = [
    url(r'^$', HostingList.as_view(), name='hosting-list'),
    url(r'^(?P<hosting_pk>\d+)/$', HostingDetail.as_view(), name='hosting-detail'),
    url(r'^(?P<hosting_pk>\d+)/photo/$', PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<hosting_pk>\d+)/photo/(?P<photo_pk>\d+)/$', PhotoDetail.as_view(), name='photo-detail'),
]