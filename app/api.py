from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from app.model import RecipeSchema, UpdateRecipeSchema

app = FastAPI()

recipes = [
    {
        "id": 1,
        "name": "Donuts",
        "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
    }
]

@app.get("/", tags=["Root"])
def get_root() -> dict:
    return {
        "message": "Welcome to your Okteto app."
    }

@app.get("/recipe", tags=["Recipe"])
def get_recipes() -> dict:
    return {
        "data": recipes
    }

@app.get("/recipe/{id}", tags=["Recipe"])
def get_recipe(id: int) -> dict:
    if id > len(recipes) or id < 1:
        return {
            "error": "Invalid ID passed."
        }

    for recipe in recipes:
        if recipe['id'] == id:
            return {
                "data": [
                    recipe
                ]
            }

    return {
        "error": "No such recipe with ID {} exist".format(id)
    }

@app.post("/recipe", tags=["Recipe"])
def add_recipe(recipe: RecipeSchema = Body(...)) -> dict:
    recipe.id = len(recipes) + 1
    recipes.append(recipe.dict())
    return {
        "message": "Recipe added successfully."
    }
  
def update_recipe(id: int, recipe_data: UpdateRecipeSchema)  -> dict:
    stored_recipe = {}
    for recipe in recipes:
        if recipe["id"] == id:
            stored_recipe = recipe
    
    if not stored_recipe:
        return {
                "error": "No such recipe exists."
            }

    stored_recipe_model = RecipeSchema(**stored_recipe)
    update_recipe = recipe_data.dict(exclude_unset=True)
    updated_recipe = stored_recipe_model.copy(update=update_recipe)
    recipes[recipes.index(stored_recipe_model)] = jsonable_encoder(updated_recipe)

    return {
        "message": "Recipe updated successfully."
    }

@app.delete("/recipe/{id}", tags=["Recipe"])
def delete_recipe(id: int) -> dict:
    if id > len(recipes) or id < 1:
        return {
            "error": "Invalid ID passed"
        }

    for recipe in recipes:
        if recipe['id'] == id:
            recipes.remove(recipe)
            return {
                "message": "Recipe deleted successfully."
            }

    return {
        "error": "No such recipe with ID {} exist".format(id)
    }
