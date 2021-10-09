# Definition of radius
r = 1.2

# Import the math package
import math

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

##### Following will calculate distance, moon is travelling if angular displacement is given.
# Distance of moon from earth (radius)
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = round(r*radians(12),2)

# Print out dist
print("Moon has travelled : " + str(dist) + "kms")