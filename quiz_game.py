print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    print(str(score))
else:
    print("Try again")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    print(str(score))
else:
    print("Try again")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
    print("Your score is " + (str(score)) + "!")
else:
    print("Try again")

print("You got " + str(score) + " questions correct!")
print("Your score was " + str((score / 3) * 100) + " %")