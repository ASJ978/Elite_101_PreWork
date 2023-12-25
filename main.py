## All dialogue is temporary, will be tweaked later

##Greet User
print("Hello, I am your chat bot assisstant!")
##Ask for name and age

name = input("What is your name? \n")
age = input("What is your age? \n")

##Ask how to help

input(f'You are {age}? I have a friend who is {age}! How can I help you {name}? \n')

##List of options on how to continue

choice = input("\nYou can choose: \n 1. placeholder1 \n 2. placeholder2 \n 3. placeholder3 \n 4. placeholder4 \n 5. exit \n")

if choice == "5":
  print(f'\nGoodbye {name}! See you next time!')
  exit()