recipes = [
    {   'title': 'Lemon Cake',
        'ingredients': ['Flour', 'Sugar', 'Butter', 'Lemons', 'Eggs'],
        'instructions': {'oven_minutes': '30', 'oven_temp': '180'}
    },

    {   'title': 'Brownie',
        'ingredients': ['Chocolate', 'Flour', 'Butter','Eggs', 'Sugar'],
        'instructions': {'oven_minutes': '20', 'oven_temp': '200'}
    },

    {   'title': 'Banana Bread',
        'ingredients': ['Bananas', 'Flour', 'yeast', 'water'],
        'instructions': {'oven_minutes': '60', 'oven_temp': '160'}
    }
]

def display_recipes():
    print('\nRECIPE BOOK')
    for i, recipe in enumerate(recipes):
        print(f"\n\t{i+1} - {recipe['title']}")

def choose_recipe(number_of_recipes) -> int:
    while True:
        print('\nWhat would you like to bake today?')
        choice = input('\nPlease input the number of your chosen recipe: ')
        if not choice:
            return None 
        elif choice.isdigit() and 0 < int(choice) <= number_of_recipes:
            return int(choice)

        print('Please pick a valid number!')

def display_instructions(recipe):
    print(f"\n{recipe.get('title')}")
    print(f"\nIngredients: {', '.join(recipe.get('ingredients', []))}")
    confirmed_ingredients = input('\nDo you have these ingredients? Please put yes/no: ')
    while True:     
        if confirmed_ingredients == 'yes':
            break
        if confirmed_ingredients == 'no':
            print()
            print('Go buy some ingredients then, and then select yes to continue with the recipe.')
            print()
            confirmed_ingredients = input('Do you have these ingredients now? Please put yes/no: ')
    print(f"\nPlease bake your {recipe.get('title')} for {recipe.get('instructions', {}).get('oven_minutes')} minutes at {recipe.get('instructions', {}).get('oven_temp')} degrees.") 
         

while True: 
    display_recipes()
    choice = choose_recipe(len(recipes))
    if not choice: 
        break
    
    display_instructions(recipes[choice-1])
    print('\nShall we try another recipe then?')




