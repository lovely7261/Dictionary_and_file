# dic="MISSISSIPPI"
# for i in dic:
#     print(dic)


count = {"M":0,"I":0,"S":0,"P":0}
dic = "MISSISSIPPI"
for i in dic:
	if i == "M":
	    count['M'] = count['M']+1
	elif i == "I":
		count['I'] = count['I']+1
	elif i == "S":
		count['S'] = count['S']+1
	elif i == "P":
		count['P'] = count['P']+1
print (count)
