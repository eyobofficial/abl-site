from django.urls import path
from . import views


app_name = 'pages'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('p-1/', views.HomeView1.as_view(), name='p1-home'),
    path('p-1/about/', views.AboutView1.as_view(), name='p1-about'),
    path('p-1/service/', views.ServiceView1.as_view(), name='p1-service'),
    path('p-1/blogs/', views.BlogsView1.as_view(), name='p1-blogs'),
    path('p-1/blog/', views.BlogDetailView1.as_view(), name='p1-blog'),
    path('p-1/contact/', views.ContactView1.as_view(), name='p1-contact'),
]
