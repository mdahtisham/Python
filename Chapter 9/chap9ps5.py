with open("sample6.txt") as f:
    content = f.read()


with open("sample6_1.txt", 'w') as f:
    f.write(content)