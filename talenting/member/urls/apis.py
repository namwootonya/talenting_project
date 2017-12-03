from django.conf.urls import url

from ..apis import SignUp, LogIn, EmailIsUnique, ProfileCreate, ProfileDetail

urlpatterns = [
    url(r'sign-up/$', SignUp.as_view(), name='sign-up'),
    url(r'log-in/$', LogIn.as_view(), name='log-in'),
    url(r'email-check/$', EmailIsUnique.as_view(), name='email-check'),
    url(r'profile/$', ProfileCreate.as_view(), name='profile-create'),
    url(r'profile/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile-detail'),
]