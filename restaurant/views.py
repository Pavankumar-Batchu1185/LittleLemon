from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request,'index.html',{})

#def menu(request):
'''
    menu_data=Menu.objects.all()
    main_data={"menu":menu_data}
    return render(request,'menu.html',{"menu":main_data})
    '''
class MenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [IsAuthenticated]