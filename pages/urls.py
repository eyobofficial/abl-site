from django.urls import path
from . import views


app_name = 'pages'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView1.as_view(), name='about'),
    path('service/', views.ServiceView1.as_view(), name='service'),
    path('contact/', views.ContactView1.as_view(), name='contact'),
]
