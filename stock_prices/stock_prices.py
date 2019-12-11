#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # MP = set initial max profit to prices[1] - prices[0]
  max_profit = prices[1] - prices[0]
 
  # iterate over items and find difference between items to the right
  for i in range(0, len(prices) - 1):
    for j in range(0, i):
      possible_profit = prices[i] - prices[j]
  # if price[i] > price[j] compare that difference to current MP
      if max_profit < possible_profit:
  # if greater then MP update MP to that value
        max_profit = possible_profit

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  