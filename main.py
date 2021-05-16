import random
def numselect():
  global dice1 #You have to declare a variable as global before giving it a value
  dice1 = random.randint(1, 6) #Gives the first dice a value
  global dice2 #You have to declare a variable as global before giving it a value
  dice2 = random.randint(1, 6) #Gives the second dice a value

cheater = False #The person always starts legimately without being a cheater

def cheat(): #The cheating fuction
  cheat = input("Would you like some help for your next try? (Maybe a little cheating)" + "\n\n") #Asks the user if they would like to cheat
  if cheat in ("yes","Yes"): #If the person choise to cheat or not
    global cheater
    cheater = True #Sets cheater status to True
    coinflip = random.randint(1,2) #Makes a coinflip to determine if it will give the correct answer or not
    if coinflip == 1: #If coinflip = 1, then the correct answer will be given
      print("\n" + "Shhh... Don't tell anyone but the answer might be " + str(sumd) + "\n")
    if coinflip == 2: #If coinflip = 2, and incorrect answer will be given
      print("\n" + "Shhh... Don't tell anyone but the answer might be " + (str(sumd + random.randint(1,2))) + " or " + (str(sumd - 1)) + "\n") #There will always be two incorrect answers, but the cheater will never know this
  if cheat in ("no","No"): #Checks if the person decided to cheat
    print("\n") #A space or neatness
    d_game() #Recalls the game functions with the person receiving no assistance

numselect() #I have to call this function in order to use the global variables
sumd = dice1 + dice2 #Sums the value of both dices

def d_game(): #Defines the function that will be called to run the game
  print("What do you think the sum between the two dices will be? \n") #Prints out the first prompt
  answer = int(input()) #Collects user response
  if answer == dice1 + dice2: #Checks if the users response matches the sum of both dices
    print("\n"+ "You are correct! Congratulations :) Play again sometime soon") #If the response matches, then it prints out nice
    return #Ends program
  else:
    if cheater == True: #Checks if the person decided to cheat in their last attempt
      print("\n" + "Cheaters never prosper") #Prints out a line calling them out on the cheating
      return #Ends the game
    if cheater == False:
      print("\nWrong answer! Type \"answer\" to view the correct answer or \"again\" to try again.\nPssst.. you have infinite tries, so don't be discouraged \n") #Provides the user two ways to continue if their initial answer is wrong
  try1 = input() #Collects their answer
  if try1 in ("Again", "again"): #Check to see if the choice was to try again 
    print("\n") #A space to make it look more organized
    #cheat()
    #d_game() #Recalls  the function, therefore, restarting the game, but the initial values remain
  if try1 in ("answer", "Answer"): #Checks to see if the choice was to receive the answer
    print("\n" + "The answer is ", str(sumd)) #Prints out the answer using the previous sum we obtained at the beginning. I added the values into one variable to make it neater
    return #Ends the game
  if cheater == False: #If the person has not decided to cheat, they will be prompted to cheat again
    cheat() #Calls the cheat function 
    d_game() #Restarts the questions

  
d_game() #Calls the function of the game to begin it