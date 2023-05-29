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


        # Create recipe object
        if recipe_name and complete_ingredient_string:
            recipe_obj = Recipe(recipe_name=recipe_name,
                            all_ingredients=complete_ingredient_string,
                            instructions=recipe_instructions)
            recipe_obj.save()


        # Make ingredients into Ingredient Objects and assign them to recipe
        for ingredient in ingredients:

            # Retrieve already existing ingredient object
            if Ingredient.objects.filter(ingredient_name=ingredient).exists():
                ingr_obj = list(Ingredient.objects.filter(ingredient_name=ingredient))[0]
            # Create new ingredient objects
            else:
                ingr_obj = Ingredient(ingredient_name=ingredient)
                ingr_obj.save()

            # Assign ingredient to recipe
            ingr_obj.recipes.add(recipe_obj)


        # print("All Recipes", Recipe.objects.all())
        # print("All Ingredients", Ingredient.objects.all())
        #
        # print("Ingredients belonging to Recipe", recipe_obj.ingredient_set.all())
        # print("Recipes with Ingredient", ingr_obj.recipes.all())


    return render(request, "recipes/add_recipe.html")

