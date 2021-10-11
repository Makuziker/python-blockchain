def filter_and_output_names():
  names = ['Brogan', 'Ives', 'Bob', 'Rosen', 'Nannon', 'Nn', 'nnnnnnnn', 'ooooooNoon']
  while len(names) > 0:
    if len(names[0]) > 5:
      if names[0].find('n') or names[0].find('N'):
        print(names[0] + ' ' + str(len(names[0])))
    names.pop(0)

filter_and_output_names()
