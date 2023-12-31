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
from django.conf.urls.static import static
from django.conf import settings

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
    path('collection_list', CollectionListView.as_view(), name='collection-list'),
    path('collection_list/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', CollectionUpdateView.as_view(), name='collection-edit'),
    path('collection_list/<pk>/delete', CollectionDeleteView.as_view(), name='collection-delete'),
    path('beyblade_list', BeybladeListView.as_view(), name='beyblade-list'),
    path('beyblade_list/add', BeybladeCreateView.as_view(), name='beyblade-add'),
    path('beyblade_list/<pk>', BeybladeUpdateView.as_view(), name='beyblade-edit'),
    path('beyblade_list/<pk>/delete', BeybladeDeleteView.as_view(), name='beyblade-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
