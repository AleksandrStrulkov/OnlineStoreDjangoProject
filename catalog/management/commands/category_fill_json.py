from django.core.management import BaseCommand
import json
from catalog.models import Category


class Command(BaseCommand):
	def handle(self, *args, **options):

		with open('category.json', 'r', encoding='utf-8') as file:
			category = json.load(file)

			category_for_create = []
			for category_item in category:
				category_i = category_item['fields']
				category_for_create.append(Category(**category_i))

			Category.objects.all().delete()
			# Category.objects.all().first()
			Category.objects.bulk_create(category_for_create)


