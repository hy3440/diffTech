from django.core.management import BaseCommand
from djangotest.models import relation

import re

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the model from the file,
first make migrations.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
	# Show this when the user types help
	help = "Loads data from relations.txt into our relation model"

	def handle(self, *args, **options):
		if relation.objects.exists():
			print('relation already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return

		else: 
			print("Loading relation data ...")
			f = open('relations.txt')
			lines = f.readlines()
			f.close()

			for line in lines:
				if line.startswith('('):
					items = []
					line = re.sub(r'[(\')]',' ',line.strip())
					line = re.sub(r'\\n',' ',line)
					items = line.strip().split(',')
					final = []
					for item in items:
						finalitem = item.strip()
						final.append(finalitem)
					Relation = relation()

					#0 and 2 form comparable pair
					pair = sorted([final[0],final[2]])
					#print(pair)
					Relation.tag = pair[0]
					Relation.simitag = pair[1]


					#1 and 3 form comparable quality
					if final[3] == '':
						quality = final[1] + ' overall'
					else:
						quality = final[1] + ' in '+ final[3]
					#print(quality)
					Relation.quality = quality

					example_id = final[4]
					example = final[5]

					#print(example_id+'\t'+example)
					Relation.example_id = example_id
					if len(example) < 400:
						Relation.example = example

						Relation.save()   

					else:
						print('example with id '+example_id + ' id too long!')    





