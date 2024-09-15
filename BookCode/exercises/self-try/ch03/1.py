import sys

input_args = sys.argv 

if len(input_args) > 1:
    print(set(input_args[1:]))