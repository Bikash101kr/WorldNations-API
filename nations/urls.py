from django.urls import include, path
from nations import views


urlpatterns = [
    path(r'^api/nations$', views.nations_list),
    path(r'^api/nations/(P<pk>[0-9]+)$', views.nations_detail)
]