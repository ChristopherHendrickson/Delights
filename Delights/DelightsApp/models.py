from django.db import models

# Create your models here.

class Ingredients(models.Model):
    Ingredient = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    unit_price = models.FloatField(default=0)
    unit = models.CharField(max_length=10)


class MenuItems(models.Model):
    item = models.CharField(max_length=200)
    price = models.FloatField(default=0)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField(default = 0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItems,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)