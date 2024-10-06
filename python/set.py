info={ 3,5,7,6,2,7,5,30}
adds={3,20,30}
print(info,adds)
print(info.difference(adds))
print(info.issuperset((adds)))
print(adds.issubset(info))
print(info.union(adds))
info.update(adds)
print(info)
lib={
    1:"kanchana,arundhath,chandramukhi",
    2:"salaar,kalki,bahubali"
}
print(lib[1])