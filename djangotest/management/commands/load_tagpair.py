from django.core.management import BaseCommand
from djangotest.models import tagpair

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
		if tagpair.objects.exists():
			print('relation already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return

		else: 
			print("Loading tagpair data ...")
			f = open('tagpairs.txt')
			lines = f.readlines()
			f.close()

			pairDict = {}

			for line in lines:
				pair = line.strip().split()
				Tagpair = tagpair()
				Tagpair.tag = pair[0]
				Tagpair.simitag = pair[1]
				Tagpair.save()




