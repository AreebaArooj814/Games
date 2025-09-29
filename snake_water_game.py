import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("comp turn: Snake(s), water(w), gun(g)?")
randNo = random.randint(1,3)
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("your's turn: Snake(s), water(w), gun(g)?\n")
a = gamewin( comp, you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("you lose!")