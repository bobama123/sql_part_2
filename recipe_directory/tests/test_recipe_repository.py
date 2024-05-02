from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe
import datetime

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data
"""

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    expected_durations = [datetime.timedelta(minutes=30), datetime.timedelta(minutes=25), datetime.timedelta(minutes=60)]

    assert len(recipes) == 3

    for idx, recipe in enumerate(recipes):
        assert recipe.id == idx + 1
        assert recipe.name in ["Burger", "Pasta", "Chips"]
        assert recipe.rating in [1, 3, 5]
        assert recipe.average_cooking_time == expected_durations[idx]


"""
When we call Recipeepository#find with an id
We get the Recipe corresponding to that id back.
"""
def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(3)
    expected_duration = datetime.timedelta(minutes=60)

    assert recipe == Recipe(3, "Chips", expected_duration, 3)