from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category


class Command(BaseCommand):
	def handle(self, *args, **options):
		category_list = [
				{
					'name_product': 'CF-100 (С1-4) 1 Вт, 100 Ом, 5%, Резистор углеродистый',
					'description_product': 'Резистор с углеродным проводящим слоем '
										   'предназначены для работы в цепях постоянного, '
										   'переменного и импульсного тока.',
					'image': '',
					'category': Category.objects.get(pk=1),
					'price': '9',
					'created_at': '2023-01-09',
					'updated_at': '2023-11-26'
				},
				{
					'name_product': '20N06 KUU полевой транзистор (MOSFET)',
					'description_product': '20N06 N-канальный полевой транзистор '
										   'для поверхностного монтажа в корпусе TO-252 (DPAK). '
										   'Напряжение сток-исток 60 Вольт, максимальный ток стока 20 А. '
										   'Сопротивление канала в открытом состоянии 38 мОм '
										   '(при Vgs=10 В, Id =10 А).',
					'image': '',
					'category': Category.objects.get(pk=2),
					'price': '12',
					'created_at': '2023-01-09',
					'updated_at': '2023-11-26'
				},
				{
					'name_product': 'Керамический конденсатор RUICHI NPO, 22 пкФ, 50 В',
					'description_product': 'Керамический конденсатор RUICHI NPO, 22 пкФ, '
										   '50 В - это конденсатор, у которого диэлектриком '
										   'служит керамика на основе главным образом титанатов '
										   'циркония, кальция, никеля и бария. Ёмкость таких '
										   'устройств от долей пикофарады до нескольких микрофарад. '
										   'Рабочее напряжение от нескольких десятков вольт до '
										   'десятков киловольт.',
					'image': '',
					'category': Category.objects.get(pk=3),
					'price': '2',
					'created_at': '2023-01-09',
					'updated_at': '2023-11-26'
				},
				{
					'name_product': '1.5KE51A MIC TVS диод (супрессор) 43.6 В, 1500 Вт, DO-201',
					'description_product': '1.5KE51A Однонаправленный TVS диод (супрессор) '
										   '43,6 Вольт выводной в корпусе DO-201 для сквозного монтажа. '
										   'Максимальная импульсная мощность рассеивания 1500 Вт. '
										   'Предназначен для защиты цепей от помех, вызванных '
										   'грозовыми разрядами, переходными процессами и прочих.',
					'image': '',
					'category': Category.objects.get(pk=4),
					'price': '12',
					'created_at': '2023-01-09',
					'updated_at': '2023-11-26'
				},
				{
					'name_product': 'RRP20-4-03-024D, Реле пром.= 24В 4пк 3А РЭК78/4 б/роз',
					'description_product': 'Реле предназначены для передачи команд управления '
										   'исполнительными элементами путем коммутации их '
										   'электрических цепей своими переключающими контактами. '
										   'Реле соединяются с розеточными модульными разъемами. '
										   'На разъемах расположены зажимы выводов переключающих '
										   'контактов и катушки.',
					'image': '',
					'category': Category.objects.get(pk=3),
					'price': '330',
					'created_at': '2023-01-09',
					'updated_at': '2023-11-26'
				},

		]

		category_for_create = []
		for category_item in category_list:
			category_for_create.append(Product(**category_item))

		Product.objects.all().delete()
		Product.objects.bulk_create(category_for_create)
		call_command('dumpdata', 'product(json)')
