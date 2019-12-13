#!/usr/bin/python

import sys

# N =  1                                [R]                                                                               [P]                                                  [S]
#       
# N =  2                       [R  R]  [R P]  [R S]                                                                [P R] [P P] [P S]                                    [S R] [S P] [S S]
# 
# N =  3  [R R R] [R R P] [R R S] [R P R] [R P P] [R P S] [R S R] [R S P] [R S S]       [P R R] [P R P] [P R S] [P P R] [P P P] [P P S] [P S R] [P S P] [P S S]

#? to get n take the value of n-1, add R in front of each list, do the same for P and S
# 
#  
# 
# ? base case
#  if n <= 0 return 0 
#  if n === 1 return 3


def rock_paper_scissors(n, plays = [['rock'], ['paper'], ['scissors']]):
  
  # base plays to add too
  round_plays = plays

  # for each possible move to add tp base plays
  possible_moves = {'rock', 'paper', 'scissors'}

  # base case
  if n == 1:
    return round_plays

  # making a copy of the list before learing to insert new values
  rp_copy = round_plays.copy()
  rp_len = len(rp_copy)

  round_plays.clear()

  x = { 'rock': [], 'paper': [], 'scissors': []}

  for i in x:
    
      for j in range(0, rp_len):
        
        round_plays.append([i, *rp_copy[j]])
        
        x[i] = round_plays
      
  return rock_paper_scissors(n - 1, round_plays)


print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

