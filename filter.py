
data = open("datafile.txt","r")


bool = 0
cs = ""
for line in data:
	if line[0] == '>':
		bool = 0
		if "mus" in line.lower() or "rat" in line.lower():
			bool=1

			cs += line

	elif bool == 1:
		cs += line

result = ""
counter = 0
pcount = 0
for char in cs:
	if char == '>':
		result += '\n' '\n' 
		counter =0
		pcount = 0

	if char != '\n':
		result+=char
		counter+=1
	if char == ']':
		result += '\n' '\n'
		counter = 0

	if pcount == 0 and char == ')':
		pcount = 1
	elif pcount == 1 and char == ')':
		result += '\n' '\n'
		counter = 0
	if counter == 60:
		result += '\n' '\n' 
		counter =0


print (result)


