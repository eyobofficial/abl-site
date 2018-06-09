from django.urls import path
from . import views


app_name = 'pages'


urlpatterns = [
    path('', views.HomeView1.as_view(), name='p1-home'),
    path('about/', views.AboutView1.as_view(), name='p1-about'),
    path('service/', views.ServiceView1.as_view(), name='p1-service'),
    path('contact/', views.ContactView1.as_view(), name='p1-contact'),
]
