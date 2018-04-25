f = open('tagpair_refined.txt','r',encoding = 'utf8')
lines = f.readlines()
f.close()

fw = open('tagpair_db.txt','w',encoding = 'utf8')
i = 0

triple = ''
triple_simi = ''
for line in lines:
	if i%3 == 0:
		#like 0,3,6,...
		fw.write(triple + ' | '+triple_simi+'\n')

		triple = ''
		triple_simi = ''
		triple += line.strip().split()[0]+'\t'
		for item in line.strip().split()[1:]:
			triple_simi += item + '\t'
		triple_simi += ',' + '\t'
		i+=1
	else:
		triple += line.strip().split()[0]+'\t'
		for item in line.strip().split()[1:]:
			triple_simi += item + '\t'
		triple_simi += ',' + '\t'
		i+=1

fw.close()
