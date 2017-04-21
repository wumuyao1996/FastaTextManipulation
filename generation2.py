
data = open("datafile.txt","r")


counter = 0
for line in data:
	if line[0] == '>':

		barCount = 0
		barSpot = 0
		k=0
		while k < len(line):
			if line[k]=="|" :
				if barCount ==1:
					barSpot = k
				barCount+=1
			k+=1


		print (line[4:barSpot], counter)###

		counter +=1
	else:
		counter+= len(line)-1

		#len(line)-1, 