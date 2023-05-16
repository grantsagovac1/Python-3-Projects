# Prints a message to the terminal
print("Welcome to my computer quiz!") 

# prompts an input asking the user if they want to play
playing = input("Do you want to play? ")

# if the answer is not equal to yes it will quit
# the .lower() method will let you type in all caps YES and still satisfy the == operator for "yes"
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

# creates an empty array score to store the score
score = 0

# prompts user with a question
answer = input("What does CPU stand for? ")

# same trick as before using the .lower() so the answer will be right whether or not they use capitals
if answer.lower() == "central processing unit":
    print("Correct!")
# adds 1 and sets a new value for the score array, then prints the score value as a string
    score += 1
    print("Your score is " + (str(score)) + "!")
else:
    print("Try again")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    print("Your score is " + (str(score)) + "!")
else:
    print("Try again")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
    print("Your score is " + (str(score)) + "!")
else:
    print("Try again")

# prints out score and tells user their score
print("You got " + str(score) + " questions correct!")
print("Your score was " + str((score / 3) * 100) + " %")
print("Great job!")