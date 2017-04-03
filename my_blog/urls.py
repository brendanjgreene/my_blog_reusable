from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^top/$', views.top_lists),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name="edit_post"),
]
