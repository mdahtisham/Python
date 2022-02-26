import random

def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer Turn : Sname(s) Water(w) or Gun(g) ")
rand = random.randint(1,3)
# print(rand)
if rand == 1:
    computer = 's'
elif rand == 2:
    computer = 'w'
elif rand == 3:
    computer = 'g'



you = input("Your's Turn : Sname(1) Water(2) or Gun(3) : ")
a = gameWin(computer, you)


print("computer choose: " + computer)
print("You choose: " + you)

if a == None:
    print("The game is Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")




