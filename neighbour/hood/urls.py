from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^home/$', views.home, name= 'home'),
    url(r'^update/profile/', views.create_profile, name="createProfile"),

]