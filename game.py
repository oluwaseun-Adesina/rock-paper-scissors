import random

options = ['R', 'P', 'S']


user_input = ''


while(user_input not in options):
    print("Type in the letter corresponding to your choice:")
    print("R for Rock")
    print("P for Paper")
    print("S for Scissors")
    user_input = input("Enter your choice: ").capitalize()   
    if(user_input in options):
        print('You chose: ' + user_input)
    else:
        print("!!! Invalid User Input: Please enter a valid input")
      

computer_input = random.choice(range(1,3))



if computer_input == 1:
    computer_input = 'R'
elif computer_input == 2:
    computer_input = 'P'
else:
    computer_input = 'S'
    
print('Computer chose: ' + computer_input)
    
if computer_input == user_input:
    print("It's a tie!")
elif computer_input == 'R' and user_input == 'S':
    print("You lose!")
elif computer_input == 'S' and user_input == 'P':
    print("You lose!")
elif computer_input == 'P' and user_input == 'R':
    print("You lose!")
else:
    print("You win!")

  
# elif computer_input == 'R' and user_input == 'P':
#     print("You win!")
# elif computer_input == 'R' and user_input == 'S':
#     print("You lose!")
# elif computer_input == 'P' and user_input == 'R':
#     print("You lose!")

