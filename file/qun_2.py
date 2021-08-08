my_file = open("people2-exercise.txt")
file_data = my_file.read()
for x in my_file:
    print (x)
my_file.close()