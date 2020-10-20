# Luke Preston
"""This program is designed to be a similar replication of the well known game
"Battleship".
The program will correctly be able to take your guess of where you think the
opponents enemy ship is and will give you a "HIT!" or "MISS" response.
If you are finally able to sink your opponents battleship, the game will
finish and you will have won!"""

# Introduction <<<<
player_name = input("Welcome to Battleship! Please enter your name. ")
print("Hi", player_name + ",", "have you played Battleship before?")

# Experience <<<<
player_experience = (input("Please enter \"Yes\" or \"No\": "))
""" sep="-->" gets rid of the whitespace in between the two strings 
and places the arrow within the quotes """

if (player_experience == "Yes"):
    print("Great!"," We have high hopes for you!", sep="-->")
elif (player_experience == "No"):
    print(" ")
    print("No worries! The goal of the game is to "
          "sink your opponents battleship!")
    print(" ")
    print("We will go over the official rules of the game board very soon.")
    print("For now, Let\'s go ahead and pick your team.")
else:
    player_experience = (input("Please enter \"Yes\" or \"No\": "))

# Red or Blue Team <<<<
team_color = input("Please pick your team. Red or Blue: ")
if (team_color == "Red"):
    print(" ")
    print("Nice choice", player_name + ".",
          "You will be going against your arch rivals, the Blue Team.")
elif (team_color == "Blue"):
    print(" ")
    print("Great pick", player_name + ".",
          "You will be going against your arch rivals, the Red Team.")
else:
    """ The int(3) prints the "Error" message three times because
    it is being multiplied """

    print("Error! " * int(3), "Please restart the program")

# Game board layout & Getting Started <<<<
continue_key = input("Press any key to continue!: ")
print(continue_key)
# End=" " provides a space for the variable x between the two strings
x = "LETS BEGIN:"
print(x, end=" ")
print("Now that you\'re all set up, let\'s show you the game board!")
print(" ")
number = 0
while (number < 100):
    number = number + 1
    print("Loading:", number, "%")
print("Finished.")
print(" ")

""" The game_board variable holds the string 0 and multiplies that string by 6. 
While being introduced to the range function that creates 6 rows. 
Therefore creating a 6x6 game board which is exactly what we want. """

game_board = (" 0 " * 6)
list_layout = game_board
for i in range(6):
    print(list_layout)
print(" ")

# Game board instructions <<<<
print("This is where you will" "guess your strikes!")
# The + is joins the two strings together in this example
print("As you can see this is a 6x" + "6 game board, there are 36 different "
      "spots you can guess.")
print(" ")

print("You will go about guessing by choosing horizontally first," 
      "starting from the bottom left 0.")
print("From there you will be able to guess vertically, going from the bottom "
      "to the top of the board.")
print(" ")
print(continue_key)

print("Here\'s an example of the list of events that will take place "
      "when guessing:")

# Game board example <<<<
print("  ")

print("For the example level we will start by giving you a clue "
      "to see where the ship lies.")
print(" ")

print("Your opponents ship is in 3 spots of one of these "
      "odd numbered rows horizontally: ")

""" The % checks to see if there is a remainder not equal
to 0 to make sure its an odd function. """

for number in range(0, 6):
    if (number % 2 != 0):
        print(number)
print(" ")
print("But your opponents ship could also be in 3 spots of one of these even "
    "numbered rows vertically: ")

""" *The % checks to see if there is a remainder equal to 0 to make 
    sure that it prints an even function 
   * The sep function fills in the white space between the variable 
    and the empty quotes with a string """

for number in range(1, 8):
    if (number % 2 == 0):
        print(number, " ", sep=" <-- Psst! Hey I think it's one of these!")

guesses_taken = 0
number1 = 2
number2 = 4
number3 = 6

while guess
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

guesses_taken = guesses_taken + 1

if guess == number1:
    print("HIT")

elif guess == number2:
    print("HIT")

elif guess == number3:
    print("HIT")
else:
    print("MISS")







