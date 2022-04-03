from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Delights.DelightsApp.models import MenuItems, Ingredients, Purchase, RecipeRequirement



# Create your views here.
class Menu(TemplateView):
    model = MenuItems
    template_name = 'DelightsApp/menu.html'

    