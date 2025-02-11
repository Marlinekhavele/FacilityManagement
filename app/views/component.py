from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from ..models import Component, InventoryLevel


class ComponentListView(ListView):
    model = Component
    template_name = "component_list.html"
    context_object_name = "components"
    paginate_by = 10

    def get_queryset(self):
        queryset = Component.objects.all()
        query = self.request.GET.get("query", "")
        level_id = self.request.GET.get("level", "")

        if query:
            queryset = queryset.filter(identifier__icontains=query)
        if level_id:
            queryset = queryset.filter(inventory_level_id=level_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["levels"] = InventoryLevel.objects.all()

        if self.request.htmx:
            self.template_name = "component_list.html"

        return context


class ComponentCreateView(CreateView):
    model = Component
    fields = ["identifier", "description", "inventory_level"]
    template_name = "add_component.html"
    success_url = reverse_lazy("component_list")

    def form_valid(self, form):
        """
        Handle form submission
        """
        self.object = form.save()
        components = Component.objects.all()[:10]

        return render(self.request, "component_list.html", {"components": components})
