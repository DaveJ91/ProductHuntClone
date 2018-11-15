from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products.views import (ProductListView, ProductDetailView,
                            ProductCreateView, ProductUpdateView,
                             ProductDeleteView,)
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='products/'), name='home' ),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('products/create', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
