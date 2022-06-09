from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from DelightsApp.models import MenuItems, Ingredients, Purchase, RecipeRequirement
from DelightsApp.forms import *
from django.views.decorators.csrf import csrf_protect


# Create your views here.
class Menu(ListView):
    model = MenuItems
    template_name = 'DelightsApp/menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list = []
        for i in context['object_list']:
             i.stock = i.in_stock()
        return context


class Inventory(ListView):
    model = Ingredients
    template_name = 'DelightsApp/inventory.html'

class Recipe(DetailView):
    
    model = MenuItems
    template_name = 'DelightsApp/recipe.html'
     
    def get_context_data(self, **kwargs):
        
        kwargs_list = []
        self_kwargs_list = []
        for key in kwargs:
            kwargs_list.append(kwargs[key])
        for key in self.kwargs:
            self_kwargs_list.append(self.kwargs[key])
        context = super().get_context_data(**kwargs)
        context={'ingredients_list':RecipeRequirement.objects.all(),'meal':kwargs['object'],'a':kwargs_list,'b':self_kwargs_list}
        return context

class Purchase_view(ListView):
    
    model = Purchase
    template_name = 'DelightsApp/purchases.html'
    def revenue(self):
        revenue=0
        for i in Purchase.objects.all():
            revenue += i.profit()
        revenue = round(revenue,2)
        return revenue

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context = {'revenue':self.revenue(),
        'purchases':Purchase.objects.all()}
        return context


class Add_Purchase_view(CreateView):
    model = Purchase
    form_class = AddPurchase
    template_name = 'DelightsApp/add_purchase.html'


def error_tests_cookied(request,cookie):
    
    if not request.session.session_key:
        request.session.create()
        request.session.save()
        

    if request.method == "POST":
        
        data = (request.POST.get('message'))    
        if str(data).strip() == 'new':
            request.session.cycle_key()
            return redirect('error_tests',cookie=request.session.session_key)
    return render(request, 'DelightsApp/error.html', {'error_msg':request.session.session_key,'cookie':request.session.session_key})

def test_index(request):


    return render(request,'DelightsApp/test_index.html',context={})