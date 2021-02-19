from django.views.generic.base import TemplateView
from django.views.generic import ListView



class AccueilView(TemplateView):
    """ That class to get the acceuil page"""
    template_name = "workshop/accueil.html"
   

class CopyrightView(TemplateView):
    """That class to give the url of all copyright use to build this site"""
    template_name = 'workshop/copyright.html'