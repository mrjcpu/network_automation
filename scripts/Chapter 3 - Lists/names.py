names = ['dora', 'alexandra', 'nani', 'raul', 'lorena']
names[1] = 'alex'
names.append('cisco')

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
motorcycles.insert(0, 'suzuki')
#print(motorcycles)
#del motorcycles[1]
#popped_motorcycle = motorcycles.pop()
#first_owned = popped_motorcycle
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
#print(motorcycles)

#print(f"The {too_expensive.title()} is too expensive for me.")
#print(first_owned)
#print(motorcycles)
#print(popped_motorcycle)
#print(f"The first motorcycle I owned was a {first_owned.title()}.")
#print(names[5].title())
print(f"My wife's name is {names[0].capitalize()}.")
#print(f"My daughters name is {names[1].capitalize()}.")
#print(f"My mother in law is {names[2].capitalize()}.")
#print(f"My good friend who teaches me the bible is {names[3].capitalize()} and his wifes name is {names[4].capitalize()}.")
