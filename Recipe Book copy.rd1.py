lines = []

with open('recipe_list.txt', 'r') as recipe_information:
    for line in recipe_information:
        if line.startswith('Recipe'):
            print(line)


recipes = {'lemon cake': ['Flour', 'Sugar', 'Butter', 'Lemons', 'Eggs'], 'brownies': ['Chocolate', 'Flour', 'Butter','Eggs', 'Sugar'], 'banana bread': ['Bananas', 'Flour', 'yeast', 'water']}
instructions = {'lemon cake': [30, 180], 'brownies': [20, 200], 'banana bread': [60, 160]}

print('RECIPE BOOK')
print()

for key, value in recipes.items():
    print (key.capitalize())
print()
print('Hello!')
choice = input('What would you like to bake today? Please input your chosen recipe: ')


while True:
    if choice in recipes.keys(): 
        break
    if choice not in recipes.keys():
        print('Please input a valid recipe!')
        choice = input('What would you like to bake today? Please input your chosen recipe: ')
        continue
    

print('You will need:')
for key, value in recipes.items():
    if choice == key:
        for ingredients in value:
            print('               ' + str(ingredients))
            print()

confirmed_ingredients = input('Do you have these ingredients? Please put yes/no: ')

while True:     
    if confirmed_ingredients == 'yes':
        break
    if confirmed_ingredients == 'no':
        print()
        print('Go buy some ingredients then, and then return to continue with the recipe.')
        print()
        confirmed_ingredients = input('Do you have these ingredients now? Please put yes/no: ')
        

for key, value in instructions.items():
        if choice == key:
            print()
            print('Bake your ' + key + ' for ' + str(value[0]) + ' minutes, at ' + str(value[1]) + ' degrees fahrenheit.')



    


