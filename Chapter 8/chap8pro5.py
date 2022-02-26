def fac(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(fac(5))

print(fac(4))

a = fac(3)
print(a)




def factRec(n):
    if n==1 or n==0:
        return 1
    return n * factRec(n-1)


f = factRec(4)
print(f)