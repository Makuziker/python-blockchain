# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.

import json
import pickle


def save_to_binary(data):
  try:
    with open('tt6.p', mode='wb') as f:
      f.write(pickle.dumps(data))
      print('saved binary to file successfully!')
  except IOError:
    print('Failed to save to file!')


def save_to_json(data):
  try:
    with open('tt6.txt', mode='w') as f:
      f.write(json.dumps(data))
      print('saved json to file successfully!')
  except IOError:
    print('Failed to save to file!')


def read_from_json():
  try:
    with open('tt6.txt') as f:
      file_content = f.readline()
      converted_data = json.loads(file_content)
      for el in converted_data:
        print(el)
  except IOError:
    print('Cannot read from file!')


def read_from_binary():
  try:
    with open('tt6.p', mode='rb') as f:
      file_content = pickle.loads(f.read())
      for el in file_content:
        print(el)
  except IOError:
    print('Cannot read from file!')


def user_interface():
  waiting_for_input = True
  input_list = []
  while(waiting_for_input):
    print('-' * 20)
    print('select an option:')
    print('1: add to list')
    print('2: save to file')
    print('3: read from file')
    print('q: quit')
    option = input('')
    if option == '1':
      input_list.append(input('Your input for the list: '))
      print('added to list!')
    if option == '2':
      print('b: Save in binary')
      print('j: Save in json')
      write_option = input('')
      if write_option == 'b':
        save_to_binary(input_list)
        input_list = []
        continue
      if write_option == 'j':
        save_to_json(input_list)
        input_list = []
        continue
      else:
        print('Invalid input')
        continue
    if option == '3':
      print('b: read from binary')
      print('j: read from json')
      read_option = input('')
      if read_option == 'b':
        read_from_binary()
        continue
      if read_option == 'j':
        read_from_json()
        continue
      else:
        print('Invalid input')
        continue
    if option == 'q':
      waiting_for_input = False
    else:
      print('Invalid input')


user_interface()