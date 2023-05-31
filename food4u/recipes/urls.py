from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes", views.recipes, name="recipes"),
    path("recipes/<str:recipe_name>", views.recipe, name="view_recipe"),
    path("add_recipe", views.add_recipe, name="add_recipe"),
    path("ingredients", views.ingredients, name="ingredients"),
    path("ingredients/<str:ingredient_name>", views.ingredient, name="view_ingredient"),
]
