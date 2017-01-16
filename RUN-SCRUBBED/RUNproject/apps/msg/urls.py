from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add_message$', views.add_message, name='add_message'),
    url(r'add_comment$', views.add_comment, name='add_comment'),
    url(r'(?P<message_id>\d+)/delete_message$', views.delete_message, name="delete_message"),
        url(r'(?P<comment_id>\d+)/delete_comment$', views.delete_comment, name="delete_comment")
]
