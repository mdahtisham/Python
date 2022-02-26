a = {}
print(type(a))

b = set()
print(type(b))

#adding values
b.add(2)
b.add(3)
b.add(9)
b.add(9)                    #It will not add because of that 9 is repeated , In set we can not repeat the values

b.add((3, 5, 1, 7))         #we can add the TUPLE
# b.add([3, 9, 1, 2,])        # but not the LIST

print(b)


print(len(b))                  # Print the length of the set

b.remove(2)
print(b)

b.pop()
print(b)
