from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe, Ingredient
from .helper_functions import get_base_ingredient, get_ingredient_string

# Create your views here.
def index(request):
    return render(request, "recipes/index.html")


def recipes(request):
    return render(request, "recipes/recipes.html")

def ingredients(request):
    return render(request, "recipes/ingredients.html")

def recipe(request):
    return HttpResponse("not yet.")




def add_recipe(request):

    if request.method == "POST":
        # print(list(request.POST.items()))
        # [('csrfmiddlewaretoken', 'QjJpZuIwFhsECwYptXPnUxtNhodXl46cc52b6XHFFi6vBbI1wZjGUlFijkgvc5D5'),
        #  ('recipe_name', ''), ('quantity_1', ''), ('measurement_1', ''), ('ingredient_1', ''), ('quantity_2', ''),
        #  ('measurement_2', ''), ('ingredient_2', ''), ('quantity_3', ''), ('measurement_3', ''), ('ingredient_3', ''),
        #  ('quantity_4', ''), ('measurement_4', ''), ('ingredient_4', '')]

        recipe_name = request.POST["recipe_name"]
        recipe_instructions = request.POST["recipe_instructions"]

        all_form_items = list(request.POST.items())[2:-1]   # this excludes token, recipe_name, and recipe_instructions

        ingredients = []
        complete_ingredient_string = ""
        for idx in range(0, len(all_form_items), 3):
            quantity = all_form_items[idx][1]
            measurement = all_form_items[idx + 1][1]
            ingredient = all_form_items[idx + 2][1]

            complete_ingredient_string += get_ingredient_string(quantity, measurement, ingredient)
            ingredients.append(get_base_ingredient(ingredient))


        recipe = Recipe(recipe_name=recipe_name,
                        all_ingredients=complete_ingredient_string,
                        instructions=recipe_instructions)
        recipe.save()

        # Ingredient.objects.filter(ingredient_name=ingredient).exists()





        print(ingredients)
        print(complete_ingredient_string)
        print(recipe_instructions)
        print(recipe_name)




    return render(request, "recipes/add_recipe.html")

