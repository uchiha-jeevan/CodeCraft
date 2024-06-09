

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('here',views.here,name='here'),
    path('basicmath',views.basicmath,name='basicmath'),
    path('add',views.add,name='basicmath'),
    # path('',views.sub,name='sub'),
    path('sub',views.sub,name='basicmath'),
    path('mul',views.mul,name='basicmath'),
    path('div',views.div,name='basicmath'),
    path('returns',views.returns,name='returns')
]
