#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

cache = {}
def eating_cookies(n, cache=None):
    
    if n <= 1 :
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
    

#     def eating_cookies_inner(num):
#     # total = 0
#       print(num)
#       if num <= 1 :
#           return 1

#       possible_takes = {1, 2, 3}
#       print('cache', cache)
#       for i in possible_takes:
#         if num - i >= 0:
#           if num not in cache:
#             cache[num] = eating_cookies_inner( num - i )
#       return cache[num]
    
#     return eating_cookies_inner(n)


# print(eating_cookies(5, {}))