with open("sample3.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%$$%$%#$")


with open("sample3.txt", "w") as f:
     f.write(content) 

