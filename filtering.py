
data = open("datafile.txt","r")


bool = 0
cs = ""
temp = ""
result = ""
counter = 0

for char in data:
	if char == '>':
		result += '\n' 
		counter =0
	
	if char != '\n':
		result+=char
		counter+=1
	
	if char == ']':
		result += '\n' '\n'
		counter = 0
	if counter == 60:
		result += '\n' '\n' 
		counter =0


print (result)


