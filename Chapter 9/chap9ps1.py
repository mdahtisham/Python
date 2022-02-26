f = open('sample3.txt')
t = f.read()
if 'coder' in t:
    print("coder is present")
else:
    print("coder not present")
f.close()