from django.urls import path, include

from . import views

urlpatterns = [
   path('', views.Menu.as_view(), name="menu"),
   path('inventory/', views.Inventory.as_view(), name="inventory"),
   path('purchases/', views.Purchase_view.as_view(), name="purchases"),
   path('recipe/<slug:slug>/', views.Recipe.as_view(), name="recipe"),
   path('purchases/new/', views.Add_Purchase_view.as_view(), name="add_purchase"),
   path('purchases/new/tests/', views.test_index),
   path('purchases/new/tests/<str:cookie>', views.error_tests_cookied, name="error_tests"),
]