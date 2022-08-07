
from nations import views
from django.urls import re_path as url 



urlpatterns = [
    url(r'^api/nations$', views.nations_list),
    url(r'^api/nations/(P<pk>[0-9]+)$', views.nations_detail)
]