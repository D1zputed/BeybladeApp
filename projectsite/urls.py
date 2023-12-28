"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beyblademasterapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('player_list', PlayerListView.as_view(), name='player-list'),
    path('player_list/add', PlayerCreateView.as_view(), name='player-add'),
    path('player_list/<pk>', PlayerUpdateView.as_view(), name='player-update'),
    path('player_list/<pk>/delete', PlayerDeleteView.as_view(), name='player-delete'),
    path('mentor_list', MentorListView.as_view(), name='mentor-list'),
    path('mentor_list/add', MentorCreateView.as_view(), name='mentor-add'),
    path('mentor_list/<pk>', MentorUpdateView.as_view(), name='mentor-update'),
    path('mentor_list/<pk>/delete', MentorDeleteView.as_view(), name='mentor-delete'),
    path('address_list', AddressListView.as_view(), name='address-list'),
    path('address_list/add', AddressCreateView.as_view(), name='address-add'),
    path('address_list/<pk>', AddressUpdateView.as_view(), name='address-update'),
    path('address_list/<pk>/delete', AddressDeleteView.as_view(), name='address-delete'),
]
