#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  # TODO possibly get each recipe key and divide by ingredients key, choose lowest number out of all possible equations
  ingredient_amounts = []

  for key in recipe:
    if ingredients.get(key) == None:
      ingredient_amounts.append(0)
    else:
      recipe_amount = recipe.get(key)
      ingredient_amount = ingredients.get(key)
      ingredient_amounts.append(ingredient_amount // recipe_amount)

  return min(ingredient_amounts)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))