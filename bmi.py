
import numpy as np

### Define height & weight
height = [1.67, 1.71, 1.55, 1.81, 1.56, 1.57, 1.65, 1.7, 1.55]
weight = [66.5, 71.0, 70.5, 75.3, 89.2, 78, 69.7, 72, 81]

### Store the heights in np_height & weight in np_weight
np_height = np.array(height)
np_weight = np.array(weight)
print(np_height)
print(np_weight)

## Calculate bmi and print it
bmi = np.around(np_weight / np_height ** 2, 2)
print('BMI : ' + str(bmi))
print('bmi belongs to ' + str(type(bmi)) + '\n' + '='*40)

## Find lightweight people
# Create the light array
light = bmi < 25

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print("We have information of total " + str(len(bmi)) + " people. Out of them, " + str (len(bmi[light])) + " are fit. \nFollowing are bmi of fit people - " + str(bmi[light]))
