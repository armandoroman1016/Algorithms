#!/usr/bin/python

# TODO try to eleminate double for loops with some sort of data structure

import argparse

def find_max_profit(prices):
  # initialize max profit 

  last_trade_idx = len(prices) - 1

  max_profit = prices[last_trade_idx] - prices[last_trade_idx - 1]

  # loop through the array compare all previous elements
  for i in range(last_trade_idx, -1, -1):
    for j in range(i - 1, -1, -1):
    # if cur value - prev value is greater than max profit update that variable
      potential = prices[i] - prices[j]

      if potential > max_profit:
        max_profit = potential

  return max_profit

  

prices = [1050, 270, 1540, 3800, 2]

print(find_max_profit(prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))