from django.shortcuts import render
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
    return render(request, "recipes/add_recipe.html")

