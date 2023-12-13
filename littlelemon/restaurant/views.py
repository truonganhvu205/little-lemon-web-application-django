from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MenuItems, Booking
from .serializers import MenuItemsSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]