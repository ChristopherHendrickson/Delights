from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from DelightsApp.models import MenuItems, Ingredients, Purchase, RecipeRequirement



# Create your views here.
class Menu(ListView):
    model = MenuItems
    template_name = 'DelightsApp/menu.html'


class Inventory(ListView):
    model = Ingredients
    template_name = 'DelightsApp/inventory.html'

class Recipe(DetailView):
    
    model = MenuItems
    template_name = 'DelightsApp/recipe.html'
     
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context={'ingredients_list':RecipeRequirement.objects.all(),'meal':kwargs['object']}    
        return context

class Purchase_view(ListView):
    
    model = Purchase
    template_name = 'DelightsApp/purchases.html'
    revenue = 0
    for i in Purchase.objects.all():
        revenue += i.profit()
    revenue = round(revenue,2)
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context = {'revenue':self.revenue,
        'purchases':Purchase.objects.all()}
        return context