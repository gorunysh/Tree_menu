from django.urls import path
from django.views.generic import TemplateView

app_name = 'menu'

urlpatterns = [
    path("<slug:title_slug>/", TemplateView.as_view(template_name="index.html"), name="menu-item"),
    path("", TemplateView.as_view(template_name="index.html")),
]