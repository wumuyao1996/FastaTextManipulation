data = open("data.in","r")

data2 = open("data.seq","r")
seq = input("Enter Sequence Here: ")

string = "".join(data2)
count = string.find(seq, 0, len(string))



result = 0
for line in data:
	pair = line.split()
	if count > int(pair[1]):
		result = (pair[0])

print(result)



# 18202068