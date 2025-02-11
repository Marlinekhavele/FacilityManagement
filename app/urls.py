from django.urls import path
from app.views.component import ComponentListView, ComponentCreateView
from app.views.Inventory_level import InventoryListView, InventoryLevelCreateView
 
urlpatterns = [
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory_create/', InventoryLevelCreateView.as_view(), name='inventory-level-create'),
    path('component_list/', ComponentListView.as_view(), name='component_list'),
    path('components_create/', ComponentCreateView.as_view(), name='components_create'),  

]

