def game():
    return 76


score = game()
with open("sample4.txt") as f:
    hiscore = int(f.read())

if hiscore<score:
    with open("sample4.txt", "w") as f:
        f.write(str(score))








