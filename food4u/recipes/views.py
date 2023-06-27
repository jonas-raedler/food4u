from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe, Ingredient
from .helper_functions import get_base_ingredient, get_ingredient_string

# Create your views here.
def index(request):
    return render(request, "recipes/index.html")


# ---------------------------------------------------------------------------------------------------------------------
# Recipe Stuff
# ---------------------------------------------------------------------------------------------------------------------

# Show list of all ingredients
def recipes(request):

    all_recipes = Recipe.objects.all().filter(cocktail=False)

    return render(request, "recipes/recipes.html", context={
        "recipes": all_recipes
    })


# Show the details of one specific recipe
def recipe(request, recipe_name):

    recipe_obj = Recipe.objects.get(recipe_name=recipe_name)

    if request.method == "POST":
        if "delete" in request.POST:
            recipe_obj.delete()
            return recipes(request)

        elif "edit" in request.POST:
            return edit_recipe(request, recipe_name)

    all_ingredients = recipe_obj.all_ingredients
    instructions = recipe_obj.instructions

    all_ingredients = all_ingredients.split(";")[:-1]
    instructions = instructions.replace("Step", "\nStep")[1:].split("\n")

    return render(request, "recipes/view_recipe.html", {
        "recipe_name": recipe_name,
        "ingredients": all_ingredients,
        "instructions": instructions
    })


def add_recipe(request, cocktail=False):

    if request.method == "POST":

        recipe_name = request.POST["recipe_name"]
        recipe_instructions = request.POST["recipe_instructions"]

        all_form_items = list(request.POST.items())[2:-1]   # this excludes token, recipe_name, and recipe_instructions

        add_recipe_to_db(recipe_name, recipe_instructions, all_form_items, cocktail)

        # print("All Recipes", Recipe.objects.all())
        # print("All Ingredients", Ingredient.objects.all())
        #
        # print("Ingredients belonging to Recipe", recipe_obj.ingredient_set.all())
        # print("Recipes with Ingredient", ingr_obj.recipes.all())

        return recipes(request)

    if cocktail:
        return render(request, "recipes/add_cocktail.html")

    return render(request, "recipes/add_recipe.html")



def edit_recipe(request, recipe_name):

    recipe_obj = Recipe.objects.get(recipe_name=recipe_name)

    if request.method == "POST":
        print(request.POST)
        if "save_changes" in request.POST:

            recipe_obj.delete()

            recipe_name = request.POST["recipe_name"]
            recipe_instructions = request.POST["recipe_instructions"]
            all_form_items = list(request.POST.items())[2:-2]  # this excludes token, recipe_name, and recipe_instructions

            add_recipe_to_db(recipe_name, recipe_instructions, all_form_items, cocktail=False)

            return recipes(request)




    ingredient_list = recipe_obj.all_ingredients
    instructions = recipe_obj.instructions

    all_ingredient_descriptions = []
    all_ingredients = ingredient_list.split(";")[:-1]

    for ingredient in all_ingredients:
        description = ingredient.split(" ")

        if len(description) > 3:
            all_ingredient_descriptions.append([description[0], description[1], " ".join(description[2:])])
        elif len(description) == 3:
            all_ingredient_descriptions.append(description)
        elif len(description) == 2:
            all_ingredient_descriptions.append([description[0], "", description[1]]) # just quantity and ingredient
        elif len(description) == 1:
            all_ingredient_descriptions.append(["", "", description[0]]) # just ingredient
        else:
            continue

    return render(request, "recipes/edit_recipe.html", context={
        "recipe_name": recipe_name,
        "ingredient_list": all_ingredient_descriptions,
        "instructions": instructions,
        "total_ingredients": len(all_ingredient_descriptions)
    })


# ---------------------------------------------------------------------------------------------------------------------
# Cocktail Stuff
# ---------------------------------------------------------------------------------------------------------------------

# Show list of all ingredients
def cocktails(request):

    all_cocktails = Recipe.objects.all().filter(cocktail=True)

    return render(request, "recipes/cocktails.html", context={
        "cocktails": all_cocktails
    })


# Show the details of one specific recipe
def cocktail(request, cocktail_name):
    recipe_obj = Recipe.objects.get(recipe_name=cocktail_name)

    all_ingredients = recipe_obj.all_ingredients
    instructions = recipe_obj.instructions

    all_ingredients = all_ingredients.split(";")[:-1]
    instructions = instructions.replace("Step", "\nStep")[1:].split("\n")

    return render(request, "recipes/view_cocktail.html", {
        "cocktail_name": cocktail_name,
        "ingredients": all_ingredients,
        "instructions": instructions
    })


def add_cocktail(request):

    return add_recipe(request, cocktail=True)



def ingredients(request):

    all_ingredients = Ingredient.objects.all()

    return render(request, "recipes/ingredients.html", {
        "all_ingredients": all_ingredients
    })


def ingredient(request, ingredient_name):

    ingredient_obj = Ingredient.objects.get(ingredient_name=ingredient_name)
    recipes_with_ingredient = ingredient_obj.recipes.all()

    return render(request, "recipes/view_ingredient.html", {
        "ingredient": ingredient_name,
        "recipes_with_ingredient": recipes_with_ingredient
    })



def add_recipe_to_db(recipe_name, recipe_instructions, ingredient_list, cocktail):

    ingredients = []
    complete_ingredient_string = ""
    print(ingredient_list)
    for idx in range(0, len(ingredient_list), 3):
        quantity = ingredient_list[idx][1]
        measurement = ingredient_list[idx + 1][1]
        ingredient = ingredient_list[idx + 2][1]

        complete_ingredient_string += get_ingredient_string(quantity, measurement, ingredient)
        ingredients.append(get_base_ingredient(ingredient))

    # Create recipe object
    if recipe_name and complete_ingredient_string:
        recipe_obj = Recipe(recipe_name=recipe_name,
                            all_ingredients=complete_ingredient_string,
                            instructions=recipe_instructions,
                            cocktail=cocktail)
        recipe_obj.save()

    # Make ingredients into Ingredient Objects and assign them to recipe
    for ingredient in ingredients:

        # Retrieve already existing ingredient object
        if Ingredient.objects.filter(ingredient_name__iexact=ingredient).exists():
            ingr_obj = Ingredient.objects.get(ingredient_name__iexact=ingredient)
        # Create new ingredient objects
        else:
            ingr_obj = Ingredient(ingredient_name=ingredient)
            ingr_obj.save()

        # Assign ingredient to recipe
        ingr_obj.recipes.add(recipe_obj)

    return




