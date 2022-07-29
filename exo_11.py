import types
class Person:
  def x():
    return 1
  def y():
    return 1
def b():
    return 2

print(isinstance(Person().x,types.MethodType))

print(isinstance(Person().y,types.MethodType))

print(isinstance(b,types.MethodType))