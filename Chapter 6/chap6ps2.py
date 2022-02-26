sub1 = int(input("sub1 marks : "))
sub2 = int(input("sub2 marks : "))
sub3 = int(input("sub3 marks : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed")

elif(sub1 + sub2 + sub3)/3 < 40:
    print("You are failed")

else:
    print("congratulation you are passed")



