from django.urls import path

from blackbox.client_config.views.menus.app_logo_view import AppLogoView
from blackbox.client_config.views.menus.menu_access_control_view import MenuAccessControlView
from blackbox.client_config.views.menus.menu_group_view import MenuGroupView

urlpatterns = [
    path('all-menus/', MenuGroupView.as_view(), name='all-menus'),
    path('menu-access-control/', MenuAccessControlView.as_view(), name='menu-access-control'),
    path('app-logo/', AppLogoView.as_view(), name='app-logo'),
]
