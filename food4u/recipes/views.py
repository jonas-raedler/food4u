from django.shortcuts import render, redirect
from django.http import HttpResponse


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


    return render(request, "recipes/add_recipe.html")

