#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  max_batches = []

  for key in recipe:

    stock_item = ingredients.get(key, None)

    if stock_item is not None:
      
      stock_item = int(stock_item)
      recipe_ing = int(recipe[f"{key}"])
      batches_possible = stock_item // recipe_ing
      max_batches.append(batches_possible)

    else:
      max_batches.append(0)
      break

  return min(max_batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))