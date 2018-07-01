from django.urls import path
from . import views


app_name = 'blogs'


urlpatterns = [
    path(
        'catagories/<slug:slug>',
        views.CatagoryDetail.as_view(),
        name='catagory-detail'
    ),
    path('', views.PostList.as_view(), name='post-list'),
    path(
        '<int:pk>/<slug:slug>',
        views.post_detail,
        name='post-detail'
    ),
]
