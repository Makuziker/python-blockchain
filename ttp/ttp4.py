# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
from functools import reduce

def format_and_print_func(math_func, *numbers):
  output = reduce(math_func, numbers, 1)
  print('Output: {:_^20.1f}'.format(output))


some_math = lambda x, y: x * y
format_and_print_func(some_math, 4, 6, 8, 1, 2)
format_and_print_func(some_math, 52, 0.4, 3, 8, 12, 0.2, 45, 0.8, 0.2)

# my_list = [1, 4, 6, 9, 1]
# reduced_list = reduce(lambda prev, curr: prev + curr, my_list, 0)
# print(reduced_list)

# my_text = 'Funds: {:_^20.2f}'.format(643.8543)
# print(my_text)

# name = 'Brogan'
# age = 24
# print(f'My name is {name} and I am {age:.1f} years old.')