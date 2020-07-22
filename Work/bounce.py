# bounce.py
#
# Exercise 1.5
height = 100
bounce_number = 1

while bounce_number <= 10:
  height = height * .6
  bounce_number += 1
  print(bounce_number, round(height, 4))