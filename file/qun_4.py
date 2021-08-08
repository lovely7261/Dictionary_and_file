my_file=open("file-question3.txt",("r"))
for i in range(18):
    c=my_file.readline()
    print(c)
    if "delhi" in c :
        Delhi=open("Delhi.txt","a")
        Delhi.write(c)
    elif "shimla" in c :
        shimla=open("shimla.txt","a")
        shimla.write(c)
    else:
        other=open("other.txt","a")
        other.write(c)






