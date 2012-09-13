#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
  # LAB(begin solution)
  count = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      count = count + 1
  return count
  # LAB(replace solution)
  # return
  # LAB(end solution)


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.

# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
  # LAB(begin solution)
  # Put each word into the x_list or the other_list.
  x_list = []
  other_list = []
  for w in words:
    if w.startswith('x'):
      x_list.append(w)
    else:
      other_list.append(w)
  return sorted(x_list) + sorted(other_list)
  # LAB(replace solution)
  # return
  # LAB(end solution)


# LAB(begin solution)
# Extract the last element from a tuple -- used for custom sorting below.
def last(a):
  return a[-1]
def sort_last(tuples):
  # +++your code here+++
  # LAB(begin solution)
  return sorted(tuples, key=last)
  # LAB(replace solution)
  # return
  # LAB(end solution)


