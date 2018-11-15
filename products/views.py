from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from products.models import Product
from django.urls import reverse_lazy

class ProductListView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
     model = Product
     fields = ['title', 'short_description', 'url']

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['short_description','url']
    template_name_suffix = '_update_form'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')
