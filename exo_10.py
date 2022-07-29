import types
def func():
    return 1

print(isinstance(func,types.FunctionType))
print(isinstance(func,types.LambdaType))