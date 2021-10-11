# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

class Food:
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind


  def __repr__(self):
    return str(self.__dict__)


  def describe(self):
    print(self.name)
    print(self.kind)

class Meat(Food):
  def cook(self):
    print('I am cooking the ' + self.name)


class Fruit(Food):
  def clean(self):
    print('I am cleaning the ' + self.name)


meat = Meat('chicken', 'meat')
meat.describe()
meat.cook()
print(meat)
fruit = Fruit('grapes', 'fruit')
fruit.describe()
fruit.clean()
print(fruit)