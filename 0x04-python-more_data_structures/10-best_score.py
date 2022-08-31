#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    winner = None
    if a_dictionary:
      for i in a_dictionary:
          if a_dictionary.get(i) > score:
              winner = i
              score = a_dictionary.get(i)
      return winner
