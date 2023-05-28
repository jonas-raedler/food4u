from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=150)
    all_ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.recipe_name



class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.ingredient_name