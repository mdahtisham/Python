file1 = "sample6.txt"
file2 = "sample6_1.txt"


with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")