import copy
dico={
    "a":"1",
    "b":2,
    "c":"la"
}

var=copy.copy(dico)
print(var)

var2=copy.copy(dico["a"]+dico["c"])
print(var2)