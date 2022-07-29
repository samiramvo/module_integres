import types
def a(x):
   yield(x) 

def b(y):
    return y

def c(a,b):
    return a+b

print(isinstance(a(345),types.GeneratorType))
print(isinstance(b(785),types.GeneratorType))
print(isinstance(c(345,788),types.GeneratorType))