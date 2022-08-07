from django.conf.urls import url
from nations import views


urlpatterns = [
    url(r'^api/nations$', views.nations_list),
    url(r'^api/nations/(P<pk>[0-9]+)$', views.nations_detail)
]