from .views import AccueilView, CopyrightView
from django.urls import path, include

app_name = "workshop"

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name="accueil"),
    path('copyright/', CopyrightView.as_view(), name="copyright"),
]
