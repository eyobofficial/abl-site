from django.urls import path
from . import views


app_name = 'blogs'


urlpatterns = [
    path('', views.BlogList.as_view(), name='post-list'),
    path('<int:pk>/<str:slug>', views.BlogDetail.as_view(), name='post-detail'),
]
