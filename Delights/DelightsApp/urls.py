from django.urls import path, include

from . import views

urlpatterns = [
   path('', views.Menu.as_view(), name="menu"),
   path('inventory/', views.Inventory.as_view(), name="inventory"),
   path('purchases/', views.Purchase_view.as_view(), name="purchases"),
   path('<slug:slug>'   , views.Recipe.as_view(), name="recipe"),
]