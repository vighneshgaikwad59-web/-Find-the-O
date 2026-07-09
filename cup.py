from random import shuffle
my=[" ","O"," "]
def my_list(my):
    shuffle(my)
    return my

def player_guess():
    guess=""
    while guess not in ("0","1","2"):
        guess =(input("enter 0,1 and 2:"))
    return int(guess)
    
def mixed(my,guess):
   if my[guess]=="O":
      print("correct")
   else:
      print("incorect")
   print("List:", my)
 
mixed_list=my_list(my)


guess=player_guess()

mixed(mixed_list,guess)