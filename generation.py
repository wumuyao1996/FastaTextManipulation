
data = open("datafile.txt","r")


bool = 0
cs = ""
for line in data:
	if line[0] == '>':
		if bool ==1 :
			cs += "@"
		bool =1

	else: 
		cs += line

print ("".join(cs.split()))


