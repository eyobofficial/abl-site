from django.urls import path
from . import views


app_name = 'pages'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
