import csv
from django.core.management import BaseCommand
from djangotest.models import tagPairCompare

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the tagPairCompare model from the CSV file,
first make migrations.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from tagpair_compare.csv into our tagPairCompare model"

    def handle(self, *args, **options):
        if tagPairCompare.objects.exists():
            print('tagPairCompare already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading tagPairCompare data ...")
        with open('tagpair_compare.csv','r') as csvfile:
        	reader = csv.reader(csvfile)
        	for row in reader:
        		print(row)
        		
        		TagPairCompare = tagPairCompare()
        		TagPairCompare.tag = row[0]
        		TagPairCompare.simiTag = row[1]
        		TagPairCompare.compare = ','.join(row[2:])
        		TagPairCompare.save()