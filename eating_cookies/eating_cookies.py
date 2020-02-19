#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution


def eating_cookies(n, cache={}):

  # if n is 0 then we can eat the cookies zero ways 
  if n < 0:
    # storing in cache in order to avoid future calls
    cache[n] = 0

  # base case
  # sets the value of cache[0] = 1 or cache[1] = 1
  # since there is only one way to eat those
  if n == 0 or n == 1:
    cache[n] = 1

  # storing values in cache to avoid unnecessary recursion
  if n not in cache:
    cache[n] = eating_cookies(n-1) + eating_cookies(n - 2) + eating_cookies(n- 3)

  return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')