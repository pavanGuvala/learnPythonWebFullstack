
mydict={
    "name":"anisha",
    "age":23,
    "likes":["cricket","football"],
    "role":"developer"
}

print(mydict)
print(mydict["age"])
print(mydict["likes"])


print(mydict.items())
print(mydict.keys())
print(mydict.values())

mydict.update({"name":"pavan"})

newdict=mydict.copy()
print(mydict)
print(newdict)
print(mydict.get("age"))
print(mydict.get("aa"))


fruits = ("Apple", "Orange")