def per(marks):
    a = ((marks[0] + marks[1] + marks[2] + marks[3])/400 ) * 100
    return a

marks1 = [72, 78, 98, 67]
per1 = per(marks1)

print(per1)


marks2 = [89, 78, 85, 69]
per2 = per(marks2)

print(per2)
