from django.urls import path

from .apps import CatalogConfig
from .views import products, home, contacts, product

app_name = CatalogConfig.name


urlpatterns = [
		path('', home, name='home'),
		path('contacts/', contacts, name='contacts'),
		path('products/', products, name='products'),
		path('<int:pk>/product/', product, name='product')

]
