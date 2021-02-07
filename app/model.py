from pydantic import BaseModel, Field
from typing import Optional, List

class RecipeSchema(BaseModel):
    name: str = Field(...)
    ingredients: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Donuts",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }

class UpdateRecipeSchema(BaseModel):
    name: Optional[str]
    ingredients: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Buns",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }
