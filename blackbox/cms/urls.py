from django.urls import path

from blackbox.core.views.profile_views import ProfileView, LoginView, RegistrationView, LogoutView, ProfileDetailsView
from blackbox.core.views.user_settings_view import UserConfirmView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('confirm-user/', UserConfirmView.as_view()),
    path('profiles/', ProfileView.as_view(), name="profile-list-view"),
    path('profiles/<int:pk>/', ProfileDetailsView.as_view(), name="profile-details-view"),
]
