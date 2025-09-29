import random
randomNumber = random.randint(1,100)
guesses = 0
userguess = None
while(userguess != randomNumber):
    userguess = int(input("Enter the number: "))
    guesses +=1
    if(userguess == randomNumber):
      print("you guess it right")
    else:
      if(userguess>randomNumber):
         print("you guess the wrong. Enter the smaller number.")
      else:
         print("you guess the wrong. Enter the larger number.")
         

print(f"you guessed the number in {guesses} guesses")

with open("hiscore.txt","r") as f:
   hiscore = int(f.read())

if (guesses<hiscore):
   print("you have just broke the hiscore")
   with open("hiscore","w") as f:
      f.write(str(guesses))
