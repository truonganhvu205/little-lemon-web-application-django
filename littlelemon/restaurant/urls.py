from django.urls import path
# from .views import index, MenuView, BookingView
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    # path('restaurant/', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]