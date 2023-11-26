from django.core.management import BaseCommand
import json
from catalog.models import Category
import psycopg2


class Command(BaseCommand):
	def handle(self, *args, **options):
		category_list = [
				{'name_category': 'Резисторы', 'description_category': 'Пассивный элемент электроцепей с постоянным '
																	   'или переменным сопротивлением. '
																	   'Предназначен для преобразования силы тока в '
																	   'напряжение, напряжения в силу тока, для '
																	   'ограничения тока, поглощения электроэнергии '
																	   'и выполнения других задач. Является компонентом'
																	   'почти всех электронных и '
																	   'электрических устройств.'},
				{'name_category': 'Транзисторы', 'description_category': 'Электронный компонент из полупроводникового '
																		 'материала, способный небольшим входным '
																		 'сигналом управлять значительным током в '
																		 'выходной цепи, что позволяет использовать '
																		 'его для усиления, генерирования, коммутации '
																		 'и преобразования электрических сигналов.'},
				{'name_category': 'Конденсаторы', 'description_category': 'Конденсатор – это устройство, способное '
																		  'накапливать и моментально отдавать '
																		  'электрический заряд'},
				{'name_category': 'Диоды', 'description_category': 'Диод-это двухполюсный электронный компонент, '
																   'который проводит ток преимущественно в одном '
																   'направлении (асимметричная проводимость)'},
				{'name_category': 'Реле', 'description_category': 'Реле — электрическое устройство (выключатель), '
																  'предназначенное для замыкания и размыкания различных'
																  ' участков электрических цепей при заданных '
																  'изменениях электрических или неэлектрических '
																  'входных величин.'},
				{'name_category': 'Датчики', 'description_category': 'Датчик - это устройство, которое выдает выходной '
																	 'сигнал с целью обнаружения физического явления.'},
				{'name_category': 'Микросхемы', 'description_category': 'Микросхема — электронная схема произвольной '
																		'сложности (кристалл), изготовленная на '
																		'полупроводниковой подложке (пластине или '
																		'плёнке) и помещённая в неразборный корпус.'},
		]

		category_for_create = []
		for category_item in category_list:
			category_for_create.append(Category(**category_item))

		Category.objects.all().delete()
		Category.objects.bulk_create(category_for_create)
