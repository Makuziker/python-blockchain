name = input('Enter your name: ')
age = input('Enter your age: ')

def print_name_and_age():
  print('name: ' + name + '\nage: ' + age)

def print_data(arg1, arg2):
  print(arg1 + arg2)

def calc_decades_lived():
  return int(age) // 10

print_name_and_age()
print_data('Hello ', 'there')
print('You have already lived ' + str(calc_decades_lived()) + ' decades.')
