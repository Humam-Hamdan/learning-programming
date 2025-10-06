# Task:
"""
Create a function that takes the number of wins,
draws and losses and calculates the number of points a football team has obtained so far.
1. wins get 3 points
2. draws get 1 point
3. losses get 0 points
"""
# Notes:
"""
Inputs will be numbers greater than or equal to 0.
"""


def football_points(wins, draws, losses):

    wins = wins * 3

    draws = draws * 1

    losses = losses * 0

    return (wins + draws + losses)



football_points(3, 4, 2)