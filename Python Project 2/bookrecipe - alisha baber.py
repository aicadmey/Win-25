from abc import ABC, abstractmethod
import os
import time
import json


# Abstract base class for recipes
class Recipe(ABC):
    def _init_(self, name, ingredients, instructions):
        self._name = name  # Encapsulated attribute
        self._ingredients = ingredients  # Encapsulated attribute
        self._instructions = instructions  # Encapsulated attribute

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def instructions(self):
        return self._instructions

    @abstractmethod
    def display_recipe(self):
        pass


# Subclass for vegetarian recipes
class VegetarianRecipe(Recipe):
    def display_recipe(self):
        print("\n--- Vegetarian Recipe ---")
        print(f"Name: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Instructions: {self.instructions}")


# Subclass for non-vegetarian recipes
class NonVegetarianRecipe(Recipe):
    def display_recipe(self):
        print("\n--- Non-Vegetarian Recipe ---")
        print(f"Name: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Instructions: {self.instructions}")


# Class to manage the recipe book
class RecipeBook:
    def _init_(self, filename="recipes.json"):
        self.recipes = []
        self.filename = filename
        self.load_recipes()

    def load_recipes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for recipe_data in data:
                    name = recipe_data["name"]
                    ingredients = recipe_data["ingredients"]
                    instructions = recipe_data["instructions"]
                    recipe_type = recipe_data["type"]

                    if recipe_type == "vegetarian":
                        recipe = VegetarianRecipe(name, ingredients, instructions)
                    else:
                        recipe = NonVegetarianRecipe(name, ingredients, instructions)

                    self.recipes.append(recipe)

    def save_recipes(self):
        data = []
        for recipe in self.recipes:
            recipe_type = "vegetarian" if isinstance(recipe, VegetarianRecipe) else "non-vegetarian"
            recipe_data = {
                "name": recipe.name,
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "type": recipe_type
            }
            data.append(recipe_data)

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully!")
        self.save_recipes()

    def view_recipes(self):
        if not self.recipes:
            print("No recipes available.")
            return
        print("\n--- Recipe Book ---")
        for i, recipe in enumerate(self.recipes, start=1):
            print(f"{i}. {recipe.name}")

    def search_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                recipe.display_recipe()
                return
        print(f"Recipe '{name}' not found.")

    def update_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                print(f"Updating recipe: {recipe.name}")
                new_name = input("Enter new name (leave blank to keep current): ").strip()
                if new_name:
                    recipe._name = new_name
                new_ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ").strip()
                if new_ingredients:
                    recipe._ingredients = new_ingredients.split(", ")
                new_instructions = input("Enter new instructions (leave blank to keep current): ").strip()
                if new_instructions:
                    recipe._instructions = new_instructions
                print(f"Recipe '{recipe.name}' updated successfully!")
                self.save_recipes()
                return
        print(f"Recipe '{name}' not found.")

    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                self.recipes.remove(recipe)
                print(f"Recipe '{recipe.name}' deleted successfully!")
                self.save_recipes()
                return
        print(f"Recipe '{name}' not found.")


# Main program
def main():
    recipe_book = RecipeBook()

    # Adding some sample recipes initially
    sample_recipes = [
        {"name": "Vegetable Salad", "ingredients": ["Lettuce", "Tomatoes", "Cucumber", "Olives"], "instructions": "Mix all ingredients and serve.", "type": "vegetarian"},
        {"name": "Chicken Curry", "ingredients": ["Chicken", "Onion", "Tomato", "Spices"], "instructions": "Cook chicken with spices and serve.", "type": "non-vegetarian"},
        {"name": "Mushroom Soup", "ingredients": ["Mushrooms", "Cream", "Garlic", "Butter"], "instructions": "Cook mushrooms in butter, add cream.", "type": "vegetarian"}
    ]

    for recipe in sample_recipes:
        name = recipe["name"]
        ingredients = recipe["ingredients"]
        instructions = recipe["instructions"]
        recipe_type = recipe["type"]

        if recipe_type == "vegetarian":
            recipe_object = VegetarianRecipe(name, ingredients, instructions)
        else:
            recipe_object = NonVegetarianRecipe(name, ingredients, instructions)
        
        recipe_book.add_recipe(recipe_object)

    while True:
        print("\n--- Recipe Book Menu ---")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipe")
        print("4. Update Recipe")
        print("5. Delete Recipe")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter recipe name: ").strip()
            ingredients = input("Enter ingredients (comma-separated): ").strip().split(", ")
            instructions = input("Enter instructions: ").strip()
            recipe_type = input("Is this a vegetarian recipe? (yes/no): ").strip().lower()

            if recipe_type == "yes":
                recipe = VegetarianRecipe(name, ingredients, instructions)
            else:
                recipe = NonVegetarianRecipe(name, ingredients, instructions)

            recipe_book.add_recipe(recipe)

        elif choice == "2":
            recipe_book.view_recipes()

        elif choice == "3":
            name = input("Enter the recipe name to search: ").strip()
            recipe_book.search_recipe(name)

        elif choice == "4":
            name = input("Enter the recipe name to update: ").strip()
            recipe_book.update_recipe(name)

        elif choice == "5":
            name = input("Enter the recipe name to delete: ").strip()
            recipe_book.delete_recipe(name)

        elif choice == "6":
            print("Exiting Recipe Book Application. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "_main_":
    main()