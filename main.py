import os
## Define a function to repeat a char
def print_block(n, string):
    double_line = '\n' + '='*n + '\n'
    print(double_line + string + double_line)

## Execute different files
print_block(60,'Executing circle.py')
os.system ("python3 circle.py")

#print ("\n=======================\nExecuting bmi.py .....\n=======================")
print_block(60,'Executing bmi.py')
os.system ("python3 bmi.py")
