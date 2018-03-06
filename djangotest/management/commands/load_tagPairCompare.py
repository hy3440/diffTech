import csv
from django.core.management import BaseCommand
from djangotest.models import tagpaircompare

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the tagPairCompare model from the CSV file,
first make migrations.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from tagpair_compare.csv into our tagPairCompare model"

    def handle(self, *args, **options):
        if tagpaircompare.objects.exists():
            print('tagPairCompare already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading tagPairCompare data ...")
        with open('tagpair_compare.csv','r') as csvfile:
        	reader = csv.reader(csvfile)
        	for row in reader:
                    print(row)
                    TagPairCompare = tagpaircompare()
                    TagPairCompare.tag = row[0]
                    TagPairCompare.simitag = row[1]
                    for item in row[2:]:
                        print(item)
                        if item != '':
                            TagPairCompare.compare += item
                            TagPairCompare.compare += ','
                        else:
                            break
                    print(TagPairCompare.compare)
                    TagPairCompare.compare = TagPairCompare.compare.replace(',',' ')
                    print(TagPairCompare.compare)
                    TagPairCompare.save()


                