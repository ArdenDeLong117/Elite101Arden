import random

greetingList = ['Whats your name?  ','Whats poppin? Whats your name?  ','Hello, whats your name?  ','Whats your name, soldier?  ']
greetingChoice = random.choice(greetingList)

userInput = input(greetingChoice)
namEE = userInput
print(f"Nice to meet you, {userInput}. My name is Tomac.")

ageList = ['How old are you?  ','Whats your age?  ','How many rotations of the Earth have you survived?(age)  ']
ageChoice = random.choice(ageList)

userInput = int(input(ageChoice))
ageNum = userInput

if ageNum < 14:
  print(f"{ageNum}? Wow youre so young!")
elif 13<ageNum and ageNum<20:
  print(f"Oooohhh the high school years!")
elif 19<ageNum and ageNum<50:
  print(f"Wow, being an adult must be great!")
else:
  print(f"{ageNum}? Dang! You must have tons of crazy experiences.")

def convo(userInput):
  if userInput == "no" or "No" or "NO":
    quit()
  while userInput == "yes" or "Yes" or "YES" or "y" or "Y":
    userInput = input(f"So what do you want to talk about now, {namEE}?  ")
    topic = userInput
    print(f"{userInput}? That sounds super interesting!")
    userInput = input(f"What exactly are/is {userInput}?  ")
    print(f"Wow you must really know alot about {topic}")
    userInput = input("Do you still want to keep talking?  ")
    convo(userInput)
  else:
    quit()

userInput = input(f"Do you want to keep talking, {namEE}?  ")
convo(userInput)

#Thank you to C2C-Elite101-PreWork-Part2 for reminding me of 
# how to use def