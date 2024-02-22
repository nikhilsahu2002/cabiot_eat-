from django.db import models

class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_delivery_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length =50,blank =True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_images/', blank=True)  
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Menu for {self.kitchen.name}"

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_item_images/', blank=True)  
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available')
    calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class DeliveryArea(models.Model):
    area_name = models.CharField(max_length=100)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='delivery_areas')

    def __str__(self):
        return self.area_name
