from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^event_page$', views.create, name='create'),
    url(r'^invite_friends$', views.invite, name='invite_friends'),
    url(r'^submit_event$', views.create_new, name="create_new"),
    url(r'^event_detail/(?P<event_id>\d+)$', views.detail, name="detail"),
]