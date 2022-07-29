from copy import deepcopy
dico={
    "a":"1",
    "b":2,
    "c":"la"
}

var=deepcopy(dico)
print(var)

var2=deepcopy(dico["a"]+dico["c"])
print(var2)