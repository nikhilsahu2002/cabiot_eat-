from django.urls import path
from .views import KitechenViewSet,DeliveryViewSet,MenuViewSet,MenuItemViewSet

urlpatterns = [
    path('kitchen',KitechenViewSet.as_view({
        "get":"GetKitechens",
        "post":"PostKitechens"
    }) ),
    path('kitchen/<str:pk>',KitechenViewSet.as_view({
        "get":"RetriveKitechens",
        "put":"UpdateKitechens",
        "delete":"DistoryKitechens"
    }) ),
    path('delivery/', DeliveryViewSet.as_view({
        'get': 'get_deliver',
        'post': 'create_deliver_area'
    }), name='delivery-list'),
    path('delivery/<int:pk>/', DeliveryViewSet.as_view({'delete': 'delete_deliver_area'}), name='delete-delivery-area'),
    
 path('menu/', MenuViewSet.as_view({
        'get': 'get_menu',
        'post': 'create_menu'
    }), name='menu-list'),
    path('menu/<int:pk>', MenuViewSet.as_view({
        'put': 'update_menu',
        "get":"RetriveMenu",
        'delete': 'delete_menu'
    }), name='menu-detail'),
    
    path('menuitem/', MenuItemViewSet.as_view({
        'get': 'get_menuItem',
        'post': 'create_menuItem'
    }), name='menuitem-list'),
    path('menuitem/<int:pk>', MenuItemViewSet.as_view({
        'put': 'update_menuItem',
        'delete': 'delete_menuItem'
    }), name='menuitem-detail'),
]
