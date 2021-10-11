# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
# 3) Use a list comprehension to check whether all persons are older than 20.
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# 5) Unpack the persons of the original list into different variables and output these variables.

persons = [
  {
    'name': 'Brogan',
    'age': 24,
    'hobbies': ['Piano', 'Coding']
  },
  {
    'name': 'Ives',
    'age': 25,
    'hobbies': ['Painting', 'TV']
  },
  {
    'name': 'Jon',
    'age': 19,
    'hobbies': ['Doing', 'Nothing']
  },
]

person_names_over_20 = [el['name'] for el in persons if el['age'] >= 20]
copied_persons = persons[:]
copied_persons[0] = { 'name': 'Jorge', 'age': 30, 'hobbies': ['Eating', 'Sleeping'] }
person1, person2, person3 = persons

print(persons)
print('-' *30)
print(person_names_over_20)
print('-' *30)
print(copied_persons)
print('-' *30)
print(person1)
print(person2)
print(person3)