from django.core.management import BaseCommand
from djangotest.models import relation

import re

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the model from the file,
first make migrations.
Then, run `python manage.py migrate` for a new empty
database with tables"""

"""
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
			f = open('relations1.txt')
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
						print('example with id '+example_id + ' example too long!')    

"""

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
			f = open('relations1.txt')
			lines = f.readlines()
			f.close()

			for ID, line in enumerate(lines):

				if (not line.startswith('(')) and line != '\n':
					print(str(ID))
					#tag line

					comparetag = line.strip().split('\t')
					
					for item in comparetag:
						print(item)
					pair = sorted([comparetag[0],comparetag[1]])
					totallength = comparetag[2]
					#counter = 0


					for i in range(int(int(totallength)/10)+1):
						Relation = relation()
						Relation.tag = pair[0]
						Relation.simitag = pair[1]
						Relation.quality = ''
						Relation.example_id = ''
						Relation.example = ''
						counter = 0

						while counter < 10:

							if (i*10+counter) < int(totallength): #if totallength 18, then maximun 17, counter = 7
							
								line = lines[ID+1+i*10+counter]
								print('line is '+line)
								counter += 1
								items = []
								line = re.sub(r'[(\')]',' ',line.strip())
								line = re.sub(r'\\n',' ',line)
								items = line.strip().split(',')
								final = []
								for item in items:
									finalitem = item.strip()
									print('finalitem : '+finalitem)
									final.append(finalitem)


								#1 and 3 form comparable quality
								if final[3] == '':
									quality = final[1] + ' overall'
								else:
									quality = final[1] + ' in '+ final[3]
								#print(quality)
								Relation.quality += quality
								Relation.quality += ','

								example_id = final[4]
								example = final[5]

								#print(example_id+'\t'+example)
								Relation.example_id += example_id
								Relation.example_id += ','
								#if len(example) < 500:
								Relation.example += example
								Relation.example += ','
							else: #counter = 10
								#counter = 0 # reset
								break

						if len(Relation.example_id) < 600 and len(Relation.quality) < 1000 and len(Relation.example) < 60000:
							Relation.save()
							print('example save!')
						else:
							print('example_id len : '+str(len(Relation.example_id)))
							print('example len : '+str(len(Relation.example)))
							print('quality len : '+str(len(Relation.quality)))
							print('above tag compare exceed model length limitation!')
													

						#Relation.save()   

					#else:
						#print('example with id '+example_id + ' example too long!')  

					#if ID != 0 : #not the first line of the file



