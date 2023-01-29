from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Designs
from django.views.generic import DetailView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    # def get(self, request):
    #     return HttpResponse("movu4 Home")


class DesignDetail(DetailView):
    model = Designs
    template_name = "design_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlists'] = Wishlist.objects.all()
        print(context["wishlists"])
        return context

class Designs_List(View):

    def get(self, reques):
        return HttpResponse("movu4 Design List")



