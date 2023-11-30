from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.
def home(request):
	return render(request, 'catalog/home.html')


def contacts(request):
	if request.method == 'POST':
		# в переменной request хранится информация о методе, который отправлял пользователь
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		# а также передается информация, которую заполнил пользователь
		print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')
	return render(request, 'catalog/contacts.html')


def products(request):
	context = {
			'object_list': Category.objects.all(),
			'title': 'Все наши комплектующие'
	}
	return render(request, 'catalog/products.html', context)


def product(request, pk):
	category_item = Category.objects.get(pk=pk)
	context = {
			'object_list': Product.objects.filter(name_category_id=pk),
			'title': f'Вы выбрали: {category_item.name_category}'
	}
	return render(request, 'catalog/product.html', context)
