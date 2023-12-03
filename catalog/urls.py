from django.urls import path

from .apps import CatalogConfig
from .views import home, contacts, one_product

app_name = CatalogConfig.name


urlpatterns = [
		path('', home, name='home'),
		path('contacts/', contacts, name='contacts'),
		# path('products/', products, name='products'),
		path('one_product/<int:pk>', one_product, name='one_product')

]
