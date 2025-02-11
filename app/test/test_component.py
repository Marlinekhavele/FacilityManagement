from django.test import TestCase
from django.urls import reverse

from ..models import Component, InventoryLevel


class ComponentCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test inventory level
        InventoryLevel.objects.create(name="test 1")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/components_create/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("components_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_component.html")

    def test_form_valid(self):
        level = InventoryLevel.objects.get(name="test 1")
        response = self.client.post(
            reverse("components_create"),
            {
                "identifier": "New Component",
                "description": "New Description",
                "inventory_level": level.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Component.objects.filter(identifier="New Component").exists())

    def test_success_url(self):
        level = InventoryLevel.objects.get(name="test 1")
        response = self.client.post(
            reverse("components_create"),
            {
                "identifier": "New Component",
                "description": "New Description",
                "inventory_level": level.id,
            },
        )
        self.assertRedirects(response, reverse("component_list"))
