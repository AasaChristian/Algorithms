#!/usr/bin/python

import argparse
prices = [100, 90, 80, 50, 20, 10]
def find_max_profit(prices):
  high_profit = 0
  for i in range(1, len(prices) ):
    current_price = i
    profit = 0
    for j in range(0, current_price):
      profit = prices[i] - prices[j]
      if high_profit == 0:
        high_profit = profit      
      if profit > high_profit:
        high_profit = profit
        
  return high_profit
      
print(find_max_profit(prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))