from re import X
import types

class per:
    def add(x):
        return x
    def mul(y):
        return y

code=compile("print('Hello","sample","exec")
print(isinstance(per().add,types.ModuleType))
print(isinstance(code,types.CodeType))