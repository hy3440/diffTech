f = open('relations.txt')
lines = f.readlines()
f.close()
count = []
for line in lines:
	if (not line.startswith('(')) and line != '\n':
		print(line.strip().split('\t'))
		for item in line.strip().split('\t')[:2]:
			if item not in count:
				count.append(item)

for item in count:
	print('\"'+item+'\"'+',')



