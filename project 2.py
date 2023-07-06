
#Rock, Paper, Scissors: Implement the classic game of Rock, Paper, Scissors
#where the user can play against the computer.
import random
attmpts=0
wins=0
while True:

    if attmpts !=5:
        random_values = random.randint(0, 2)
        name = ['rock', 'paper', 'scissors']
        comp_choice = name[random_values]
        attmpts += 1
        user_choice = input('what is your choice')
        print(f"User's choice is {user_choice} and computer's choice is {comp_choice}")
        if comp_choice==user_choice:
            print('it is a tie')
        elif (comp_choice=='rock'and user_choice=='paper')or (comp_choice=='paper'and user_choice=='scissors') or (comp_choice=='scissors'and user_choice=='rock'):
            print('user wins')
            wins+=1
        else:
            print('user loses')

    else:
        print(f'user has won {wins}times')
        break


