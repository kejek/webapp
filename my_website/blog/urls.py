from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
]
