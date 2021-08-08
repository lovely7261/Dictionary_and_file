# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

i=0
j={}
while i<3 :
    S_N=(input("enter the student name"))
    S_M=int(input("enter the marks"))
    j[S_N]=S_M
    i+=1
    print(j)
