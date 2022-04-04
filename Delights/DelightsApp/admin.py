from django.contrib import admin

# Register your models here.
from .models import *

class DelightsAppAdminRecipe(admin.ModelAdmin):
    list_display = ("menu_item","ingredient")

    
class DelightsAppAdminItem(admin.ModelAdmin):
    list_display = ("item","price")

class DelightsAppAdminPurchase(admin.ModelAdmin):
    list_display = ("menu_item","time_stamp")

admin.site.register(RecipeRequirement, DelightsAppAdminRecipe)
admin.site.register(MenuItems, DelightsAppAdminItem)
admin.site.register(Purchase, DelightsAppAdminPurchase)