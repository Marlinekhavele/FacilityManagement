from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from ..models import InventoryLevel

class InventoryListView(ListView):
    model = InventoryLevel
    template_name = 'inventory_list.html'
    context_object_name = 'inventory_levels'


class InventoryLevelCreateView(CreateView):
    model = InventoryLevel
    fields = ['name', 'parent']
    template_name = 'add_inventory_level.html'
    success_url = reverse_lazy('inventory_list')

    def form_valid(self, form):
        self.object = form.save()
        inventory_levels = InventoryLevel.objects.all()
        return render(self.request, 'inventory_list.html', {'inventory_levels': inventory_levels})


