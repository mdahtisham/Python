letter = '''Dear <|Name|>,
You are selected

Date: <|Date|>
'''
name = input("Enter your Name\n")
date = input("Enter your Date\n")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)