#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  cache = {}
  if n <= 0 or n == 1:
      return 1

  total = 0

  possible_takes = {1, 2, 3}

  for i in possible_takes:
    if n - i >= 0:
      total += eating_cookies( n - i )

  return total
print(eating_cookies(5))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# def eating_cookies(n, cache=None):

#   def find_factorial(num):
#       factorial = 1
#       for i in range( 1, n + 1 ):
#           factorial *= i
#       num = factorial

#   if n <= 1:
#     return 1


#   return eating_cookies(n // 6 * find_factorial( n - 6 )) + eating_cookies( n // 2 * find_factorial(n - 2) )  + eating_cookies(n // 1)