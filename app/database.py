from pymongo import MongoClient
from bson import ObjectId
from decouple import config

connection_details = config("DB_HOST")

client = MongoClient(connection_details)

database = client.recipes

recipe_collection = database.get_collection('recipes_collection')

def parse_recipe_data(recipe) -> dict:
    return {
        "id": str(recipe["_id"]),
        "name": recipe["name"],
        "ingredients": recipe["ingredients"]
    }

def save_recipe(recipe_data: dict) -> dict:
    recipe = recipe_collection.insert_one(recipe_data).inserted_id
    return {
        "id": str(recipe)
    }

def get_single_recipe(id: str) -> dict:
    recipe = recipe_collection.find_one({"_id": ObjectId(id)})
    if recipe:
        return parse_recipe_data(recipe)

def get_all_recipes() -> list:
    recipes = []
    for recipe in recipe_collection.find():
        recipes.append(parse_recipe_data(recipe))

    return recipes

def update_recipe_data(id: str, data: dict):
    recipe = recipe_collection.find_one({"_id": ObjectId(id)})
    if recipe:
        recipe_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

def remove_recipe(id: str):
    recipe = recipe_collection.find_one({"_id": ObjectId(id)})
    if recipe:
        recipe_collection.delete_one({"_id": ObjectId(id)})
        return True
