from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
HTTP_400_BAD_REQUEST
from rest_framework import viewsets
from.serializers import KitchenSerializer,DeliveryAreaSerializer, MenuItemSerializer,MenuSerializer
from .models import Kitchen,DeliveryArea,Menu,MenuItem
# Create your views here.

class KitechenViewSet(viewsets.ViewSet):
    def GetKitechens(self,req):
        kitchens = Kitchen.objects.all()
        serializer = KitchenSerializer(kitchens,many =True)
        return Response(serializer.data)
    
    def PostKitechens(self,req):
        serializer = KitchenSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)
    
    def RetriveKitechens(self,req,pk=None):
       try:
            kitchen = Kitchen.objects.get(id=pk)
            serilizer = KitchenSerializer(kitchen)
            return Response(serilizer.data)
       except kitchen.DoesNotExist:
            return Response({"message":"not exist"}, status=HTTP_404_NOT_FOUND)
       
    def UpdateKitechens(self,req,pk=None):
        kitchen = Kitchen.objects.get(id=pk)
        serializer = KitchenSerializer(instance=kitchen,data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)

    def DistoryKitechens(self, request, pk=None):
        try:
            kitchen =Kitchen.objects.get(id=pk)
            kitchen.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except kitchen.DoesNotExist:
            return Response({"detail": "Product not found."}, status=HTTP_404_NOT_FOUND)

class MenuViewSet(viewsets.ViewSet):
    def get_menu(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    
    def create_menu(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def RetriveMenu(self,req,pk=None):
       try:
            kitchen = Menu.objects.get(id=pk)
            serilizer = MenuSerializer(kitchen)
            return Response(serilizer.data)
       except kitchen.DoesNotExist:
            return Response({"message":"not exist"}, status=HTTP_404_NOT_FOUND)
       
    def delete_menu(self, request, pk=None):
        try:
            menu = Menu.objects.get(pk=pk)
            menu.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found'}, status=HTTP_404_NOT_FOUND)

    def update_menu(self, request, pk=None):
        try:
            menu = Menu.objects.get(pk=pk)
            serializer = MenuSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found'}, status=HTTP_404_NOT_FOUND)

class MenuItemViewSet(viewsets.ViewSet):
    def get_menuItem(self, request):
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        return Response(serializer.data)
    
    
    
    def create_menuItem(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete_menuItem(self, request, pk=None):
        try:
            menu = MenuItem.objects.get(pk=pk)
            menu.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found'}, status=HTTP_404_NOT_FOUND)

    def update_menuItem(self, request, pk=None):
        try:
            menu = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response({'error': 'Menu not found'}, status=HTTP_404_NOT_FOUND)



class DeliveryViewSet(viewsets.ViewSet):
    def get_deliver(self, request):
        delivery_areas = DeliveryArea.objects.all()
        serializer = DeliveryAreaSerializer(delivery_areas, many=True)
        return Response(serializer.data)
    
    def create_deliver_area(self, request):
        serializer = DeliveryAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # The serializer will handle associating the delivery area with the correct kitchen
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def delete_deliver_area(self, request, pk=None):
        try:
            delivery_area = DeliveryArea.objects.get(pk=pk)
            delivery_area.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except DeliveryArea.DoesNotExist:
            return Response({'error': 'Delivery area not found'}, status=HTTP_404_NOT_FOUND)