##4-3
#numbers = []
#for number in range(1, 11):
#    numbers.append(number)

#print(numbers)

##4-4
#numbers = []
#for number in range(1, 1000001):
#    numbers.append(number)

#print(numbers)

##4-5 Summing a Million
#numbers = []
#for number in range(1, 1000001):
#    numbers.append(number)

#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

##4-6 Odd Numbers
#odd_numbers = list(range(1, 20, 2))
#print(odd_numbers)

##4-7 Threes
#x3 = [value*3 for value in range(3, 30)]
#print(x3)

##4-8 Cubes
#squared = []
#for value in range(1, 11):
#    squared.append(value**2)

#print(squared)

##4-9 Cube Comprehension
#cube = [value*10 for value in range(1, 51)]
#print(len(cube))
#print(cube)

##4-10 Slices
#cube = [value*10 for value in range(1, 21)]
#print(cube)
#print(cube[len(cube)//2 -1])
#print(cube[len(cube)//2 + 2])
#print(f"The first three items in the list are: {cube[:3]}")
#print(f"Three items in the list are: {cube[len(cube)//2 - 1 : len(cube)//2 + 2]}")
#print(f"The last three items in the list are: {cube[-3:]}")

##4-11 My Pizzas, Your Pizzas
#my_pizzas = ['pepperoni', 'sausage', 'chicken', 'marguerita']
#friends_pizzas  =my_pizzas[:]

#my_pizzas.append('hawaiian')
#friends_pizzas.append('meat lovers')

#print(my_pizzas)
#for pizza in my_pizzas:
#    print(f"I love {pizza.title()}")

#print(f"I love Pizza!!!")

#print(friends_pizzas)
#for pizza in friends_pizzas:
#    print(f"My friends love {pizza.title()}")

#print(f"My friends love Pizza!!!")

##4-12 More Loops
#my_foods = ['pizza', 'falafel', 'carrot cake']
#friends_foods  =my_foods[:]

#my_foods.append('cannoli')
#friends_foods.append('ice cream')

#for foods in my_foods[-1:]:
#    print(foods.title())

#for foods in friends_foods[-1:]:
#    print(foods.title())

##4-13 - Buffet (Tuples)
buffet_foods = ('mashed potatoes', 'gravy', 'chicken', 'corn', 'prime rib')
for food in buffet_foods:
    print(food.title())

buffet_foods = ('mashed potatoes', 'gravy', 'roast beef', 'carrots', 'turkey')
for modified_food in buffet_foods:
    print(modified_food.title())