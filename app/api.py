from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from app.model import RecipeSchema, UpdateRecipeSchema
from app.database import save_recipe, get_all_recipes, get_single_recipe, update_recipe_data, remove_recipe

app = FastAPI()

@app.get("/", tags=["Root"])
def get_root() -> dict:
    return {
        "message": "Welcome to your Okteto app."
    }

@app.get("/recipe", tags=["Recipe"])
def get_recipes() -> dict:
    recipes = get_all_recipes()
    return {
        "data": recipes
    }

@app.get("/recipe/{id}", tags=["Recipe"])
def get_recipe(id: str) -> dict:
    recipe = get_single_recipe(id)
    if recipe:
        return {
            "data": recipe
        }
    return {
        "error": "No such recipe with ID {} exist".format(id)
    }

@app.post("/recipe", tags=["Recipe"])
def add_recipe(recipe: RecipeSchema = Body(...)) -> dict:
    new_recipe = save_recipe(recipe.dict())
    return new_recipe
    return {
        "message": "Recipe added successfully."
    }
  
@app.put("/recipe", tags=["Recipe"])
def update_recipe(id: str, recipe_data: UpdateRecipeSchema)  -> dict:
    if not get_single_recipe(id):
        return {
            "error": "No such recipe exist"
        }

    update_recipe_data(id, recipe_data.dict())

    return {
        "message": "Recipe updated successfully."
    }

@app.delete("/recipe/{id}", tags=["Recipe"])
def delete_recipe(id: str) -> dict:
    if not get_single_recipe(id):
        return {
            "error": "Invalid ID passed"
        }


    remove_recipe(id)
    return {
        "message": "Recipe deleted successfully."
    }