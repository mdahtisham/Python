myDict = {
    "fast": "In a Quick manner",
    "code": " a coder",
    "marks": [2,3,4],

    "anotherDict": {'pro': 'program'},
    1 :  2


}
print(myDict.keys())                    #for key
print(list(myDict.keys()))

print(myDict.values())                  # for meaning

print(myDict.items())                   # for both



print(myDict)
updateDict = {
    "hello": "world",
    "myfirst": "program",
    "marks": [8,6,1],               #reset the value, because it is already in Dict
}
myDict.update(updateDict)
print(myDict)




print(myDict.get("code"))
print(myDict["code"])

print(myDict.get("code2"))           # Return the NONE 
print(myDict["code2"])               # throwing anm ERROR