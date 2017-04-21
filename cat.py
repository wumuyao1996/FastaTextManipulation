
data = open("datafile.txt","r")

counter = 0
for line in data:
	if line[0] == '>':
		if counter != 0:
			print (counter)
		counter=0
		print (line),###
	else:
		counter+= len(line)-1

		#len(line)-1, 