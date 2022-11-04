import random

# Rock Paper or Scissors
def gameWin(comp,you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
       
print("comp turn: Rock(r) Paper(p) or Scissors(s)? ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo== 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'


you=input("Your turn: Rock(r) Paper(p) Scissors(s)? ")


print(f"computer choose {comp}")
print(f"you choose {you}")


game_result=gameWin(comp,you)
if game_result == None:
    print("The game is tie!")
elif game_result == True:
    print("You Win!")
elif game_result == False:
    print("You Loss!")

