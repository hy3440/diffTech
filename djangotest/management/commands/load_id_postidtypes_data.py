from django.core.management import BaseCommand

from pytz import UTC
from djangotest.models import id_postidtypes


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from id_postidtype into our id_postidtype model"
    

    def handle(self, *args, **options):
        
        if id_postidtypes.objects.exists():
            print('id_postidtype exists already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
    
        print("Loading tags data for id_postidtype available on stackoverflow")
        for i in range(3):
            id_postidtype = id_postidtypes()
            id_postidtype.postid = str(i)
            id_postidtype.postidtype = str(i)+'p'
            id_postidtype.save()
