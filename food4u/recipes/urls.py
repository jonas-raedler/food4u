from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("recipes", views.recipes, name="recipes"),
    path("recipes/<str:recipe_name>", views.recipe, name="view_recipe"),
    path("add_recipe", views.add_recipe, name="add_recipe"),
    path("edit_recipe/<str:recipe_name>", views.edit_recipe, name="edit_recipe"),

    path("cocktails", views.cocktails, name="cocktails"),
    path("cocktails/<str:cocktail_name>", views.cocktail, name="view_cocktail"),
    path("add_cocktail", views.add_cocktail, name="add_cocktail"),

    path("ingredients", views.ingredients, name="ingredients"),
    path("ingredients/<str:ingredient_name>", views.ingredient, name="view_ingredient"),
]
