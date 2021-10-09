# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [212, 101.7],
            [219, 88.5],
            [198, 75.8]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 4th row of np_baseball
print('Details of 4th player : ' + str(np_baseball[3,:]))

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 6th player
print('Height of last player : ' + str(np_baseball[-1,0]))

# Create numpy array: conversion
conversion = np.array ([2.54, 0.453592])

# Print out product of np_baseball and conversion
print ('Details of players in lb systems : \n' + str(np_baseball/conversion))