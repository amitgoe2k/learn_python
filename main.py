import os
## Define a function to repeat a char
def print_block(n, string):
    double_line = '\n' + '='*n + '\n'
    print(double_line + string + double_line)

## Execute different files
files = ['circle.py', 'bmi.py', '2d_array.py']
for x in files:
  print_block(60,'Executing ' + x)
  command = 'python3 ' + str(x)
  os.system (command)

