from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('', index, name='index'),
    path('api/menu-items/', MenuItemView.as_view(), name='MenuItemView'),
    path('api/menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]