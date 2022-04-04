from django.db import models
from django.urls import reverse

# Create your models here.
# models
class Ingredients(models.Model):
    Ingredient = models.CharField(unique=True,max_length=200)
    quantity = models.FloatField(default=0)
    unit_price = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    def __str__(self):
        return self.Ingredient.title()


class MenuItems(models.Model):
    item = models.CharField(unique=True,max_length=200)
    price = models.FloatField(default=0)
    slug = models.SlugField()
    
    def total_cost(self):
        cost_sum = 0
        ingredients = RecipeRequirement.objects.filter(menu_item=self)
        for i in ingredients:
            cost_sum+=i.cost()
        return round(cost_sum,2)
        
    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("recipe", kwargs={"slug": self.slug})

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField(default = 0)
    slug = models.SlugField()
    
    def get_unit_price(self):
        return self.ingredient.unit_price

    def get_unit(self):
        return self.ingredient.unit

    def amount_available(self):
        return self.ingredient.quantity

    def cost(self):
        quantity = self.quantity
        unit_price = self.get_unit_price()
        cost = quantity * unit_price
        return round(cost,2)






class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItems,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def profit(self):
        return round(self.menu_item.price - self.menu_item.total_cost(),2)



