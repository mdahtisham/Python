# with open("sample5.txt") as f:
#     content = f.read()

#     if 'python' in content.lower():
#         print("Yes python is present")
#     else:
#         print("No python is present")



content = True
i = 1
with open("sample5.txt") as f:
    while content:
        content = f.readline()
        print(content)

        if 'python' in content.lower():
            print(content)
            print("Yes python is present")
            print(i)
            i+=1
       