from django.urls import path
from . import views


app_name = 'blogs'


urlpatterns = [
    path('', views.BlogList.as_view(), name='blog-list'),
    path('<int:pk>', views.BlogDetail.as_view(), name='blog-detail'),
]
