from django.urls import path
from django.views.generic import RedirectView
from cms.views.landing import index, admin

from cms.views.app_configs.config_views import AppConfigDetailsView, AppConfigCreateView
from cms.views.app_configs.search_views import SearchListView
from cms.views.pages.content_views import ContentListView, ContentCreateView, ContentDetailsView
from cms.views.pages.page_views import PageListView, PageDetailsView

urlpatterns = [
    path('', index),
    path('admin/', admin),
    path('api/pages/', PageListView.as_view(), name='page-list'),
    path('api/pages/<str:slug>/', PageDetailsView.as_view(), name='page-details'),
    path('api/contents/', ContentListView.as_view(), name='content-list'),
    path('api/contents/<str:slug>/', ContentDetailsView.as_view(), name='content-details'),
    path('api/create-content/', ContentCreateView.as_view(), name='content-create'),
    path('api/app-config/', AppConfigDetailsView.as_view(), name='app-config-view'),
    path('api/create-app-config/', AppConfigCreateView.as_view(), name='app-config-create-view'),
    path('api/search/', SearchListView.as_view(), name='search-view')
]
