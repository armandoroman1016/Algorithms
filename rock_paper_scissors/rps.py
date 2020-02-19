#!/usr/bin/python

import sys


def rock_paper_scissors(n):

  if n <= 1:
    return [['rock'], ['paper'], ['scissors']]

  def generate_permutations(moves):
      perms = []
      choices = ['rock', 'paper', 'scissors']
      copy = moves
      
      for i in range(len(choices)):
        for j in range(len(copy)):
          new_perm = [choices[i]] + copy[j]
          perms.append(new_perm)

        copy = moves

      return perms

  n_moves = rock_paper_scissors(n - 1)

  return generate_permutations(n_moves)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')