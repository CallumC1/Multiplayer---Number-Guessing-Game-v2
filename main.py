# # File Imports
import register as r
import login as l
import time
import datetime as dt
import leaderboard as lb

import random

#Generates the date & time for LeaderBoard useage
today = dt.datetime.now()
date_time = today.strftime("%d/%m/%Y")

# randomNum = random.randint(1, 100)
# guess = None

playerAccount1 = "{playerAccount1}" #Account Names
playerAccount2 = "{playerAccount2}"

players = 0 # Players logged in | | | Set to "2" to override. | | | "0" to set to default
gameStarted = False

# Checking File Integrity 
# userAccounts.txt, leaderboard.txt
try:
    f = open("userAccounts.txt", "x")
    print("userAccounts.txt - File Not Found, New file created!")
except FileExistsError:
    pass

try:
    f = open("leaderboard.txt", "x")
    print("leaderboard.txt - File Not Found, New file created!")
except FileExistsError:
    pass


# Used to check if the guess is within 5 digits either side, too high / low or correct!
def checkGuess(guess, randomNum, guessCount):
  lowerBound = randomNum - 5
  upperBound = randomNum + 5
  # print(f"Testing: LB: {lowerBound}")
  # print(f"Testing: UB: {upperBound}")

  if guess < randomNum:
    print("\nGuess is too low")
    if guess <= upperBound and guess >= lowerBound:
      print("You are close to the number!")
    return guessCount + 1
  
  elif guess > randomNum:
    print("\nGuess is too high")
    if guess <= upperBound and guess >= lowerBound:
      print("You are close to the number!")

    return guessCount + 1
  else:
    print(f"Correct! The answer was {guess}")
    return guessCount

    
# Handles the players turns & guess inputs

def game():
  guess = None
  # Scores below are added to over the whole game
  p1_score = 0
  p2_score = 0

  
  for i in range(5):
    # Guess counts get reset every round.
    p1_guess_count = 0
    p2_guess_count = 0

    randomNum = random.randint(1, 100) # generates a random number 
    while randomNum != guess:
      # while 1: requires the user to enter a numeric value before it continues.
      while 1:
        try:
          guess = int(input(f"\n{playerAccount1} - Enter an number from 1 to 100: "))
          break # Breaks to next 
        except ValueError:
          print("Invalid Value Entered!")
          continue # Continues loop

      # The function below checks the guess & retuens the guess count value if necessary. 
      p1_guess_count = checkGuess(guess, randomNum, p1_guess_count)



    #! Player 2 Code below:
    # Generates a new number for them to guess.
    randomNum = random.randint(1, 100)
    while randomNum != guess:
      # while 1: requires the user to enter a numeric value before it continues.
      while 1:
        try:
          guess = int(input(f"\n{playerAccount2} - Enter an number from 1 to 100: "))
          break # Breaks to next 
        except ValueError:
          print("Invalid Value Entered!")
          continue # Continues loop

      # The function below checks the guess & retuens the guess count value if necessary. 
      p2_guess_count = checkGuess(guess, randomNum, p2_guess_count)


    # The below code executes at each round. The player with the least guesses scores a point
    #? Make a system so the player gets more points if they use less guesses?
    if p2_guess_count > p1_guess_count:
      p1_score += 1
      winMsg1 = (f"{playerAccount1} wins round {i +1} with {p1_guess_count} guesses.")
      winMsg2 = (f"{playerAccount2} used {p2_guess_count}.")
    elif p1_guess_count > p2_guess_count:
      p2_score += 1
      winMsg1 = (f"{playerAccount2} wins round {i +1} with {p2_guess_count} guesses.")
      winMsg2 = (f"{playerAccount1} used {p1_guess_count}.")
    
    # Displays scores at end of each round.
    print(f"""
    Round Finished... (Round {i+1}) / 5
    {winMsg1}
    {winMsg2}
    
    Current Game Scores: 
    {playerAccount1} Score: {p1_score}
    {playerAccount2} Score: {p2_score}
    
    """)

    
  # The code below runs when the games 5 rounds are finished.
  # This writes the players score into the leaderboard file along with their score.
  if p1_score > p2_score:
    f = open("leaderboard.txt", "a")
    f.write(f"\n{date_time} {playerAccount1} {p1_score}")
    f.close()
  elif p2_score > p1_score:
    f = open("leaderboard.txt", "a")
    f.write(f"\n{date_time} {playerAccount2} {p2_score}")
    f.close()

#
# LOGIN MENU BELOW
#
p1_loginmsg = "Login by typing: (1)" # Makes the login menu change
p2_loginmsg = "Login by typing: (2)"

while players < 2 or gameStarted == False:
  login_message = input(f'''Hello this is a 2 player number guessing game.
The player who uses the least guesses wins.

  Player 1 - {p1_loginmsg}
  Player 2 - {p2_loginmsg}
  Dont have an account? Type (3) to register!
  Show leaderboard: (4)

  Both players logged in? Play by typing: (5)

  Option: ''')
  if login_message == "1":
    playerAccount1 = l.login() # Authorising Account
    p1_loginmsg = f"Logged in as {playerAccount1}"
    players += 1
  elif login_message == "2":
    playerAccount2 = l.login()
    p2_loginmsg = f"Logged in as {playerAccount2}"
    players += 1
  elif login_message == "3":
    r.register()
  elif login_message == "4":
    lb.show()
  elif login_message == "5" and players == 2:
    # Start the game
    print("\nPlease wait... Starting game!\n")
    time.sleep(0.5)
    gameStarted = True
    game() 
  elif login_message == "5" and players != 2:
    print("Not enough players logged in!\n")
    time.sleep(0.9)
  else:
    print("Input not found! Re-try!")