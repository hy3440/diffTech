from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from djangotest.models import tags
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from tags_data.csv into our Pet model"

    def handle(self, *args, **options):
        if tags.objects.exists():
            print('Tags data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        """print("Creating tags data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vaccine(name=vaccine_name)
            vac.save()"""
        print("Loading tags data for tag available on stackoverflow")
        for row in DictReader(open('./tags_data.csv')):
            tag = tags()
            tag.Tag = row['Tag']
            tag.Category = row['Category']
            tag.TagWiki = row['TagWiki']
            #raw_submission_date = row['submission date']
            #submission_date = UTC.localize(
            #datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            #pet.submission_date = submission_date
            tag.save()
            #raw_vaccination_names = row['vaccinations']
            """vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            for vac_name in vaccination_names:
                vac = Vaccine.objects.get(name=vac_name)
                pet.vaccinations.add(vac)"""
            #pet.save()
