from lib.recipe import Recipe
import datetime

"""
Recipe constructs with a id, name, average_cooking_time and rating
"""

def test_recipe_constructs():
    recipe = Recipe(1, "Burger", datetime.timedelta(minutes=30), 5)
    assert recipe.id == 1
    assert recipe.name == "Burger"
    assert recipe.average_cooking_time == datetime.timedelta(minutes=30)
    assert recipe.rating == 5


