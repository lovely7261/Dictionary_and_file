states_capitals = {
  'Gujarat' : 'Gandhinagar',
  'Maharashtra' : 'Mumbai',
  'Rajasthan' : 'Jaipur',
  'Bihar' : 'Patna'
  }
for state in states_capitals:
      print(state) 
  

print("Iterate through all values:-")

states_capitals = {
    'Gujarat' : 'Gandhinagar',
    'Maharashtra' : 'Mumbai',
    'Rajasthan' : 'Jaipur',
    'Bihar' : 'Patna'
    }

for state in states_capitals:
    print(states_capitals[state])


details ={
    "name":  "Bijender",
    "age":  17,
    "class":  "10th"
    }
for x in details.values():
    print(x) 



movie ={
    "name":  "Puli",
    "hero":  "Vijay",
    "rating":  7.5
    }
for x,y in movie.items():
    print(x,y) 

print("Dictionary length") 

meal ={
    "monday":  "Chole chawal",
    "sunday":  "Fried rice",
    "wednesday":  "dosa"
    }
print(len(meal)) 