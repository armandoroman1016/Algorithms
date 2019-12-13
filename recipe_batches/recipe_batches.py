#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  # TODO possibly get each recipe key and divide by ingredients key, choose lowest number out of all possible equations
  # TODO if ingredient amounts gets a zero added return 0 immediately
    # ingredient_amounts = []
    count = 0
    max_batches = 0
    for key in recipe:
        recipe_amount = recipe.get(key)
        ingredient_amount = ingredients.get(key)
        if count == 0:
          max_batches = ingredient_amount // recipe_amount
        else:
            if max_batches == 0:
                break
                return
            else:  
                if ingredient_amount == None:
                    max_batches = 0
                    break
                    return
                elif max_batches > ingredient_amount // recipe_amount:
                     max_batches = ingredient_amount // recipe_amount

        count += 1

    return max_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 98, 'butter': 100, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))