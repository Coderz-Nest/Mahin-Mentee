#question[Guessing Game: Write a program where the computer generates a random number, and the user has to guess it.
# The program provides hints like "too high" or "too low" until the user guesses  the correct number.]

#prepration of code
import random
random_value = random.randint(1 , 100)
atempts=0
while True:
    value= float(input(' what is your guess'))
    atempts+=1
    if atempts == 5:
        print('out of reach')
        break
    elif value > random_value and atempts<5:
        print('To High')
    elif value < random_value and atempts<5:
        print('to low')

    else:
        print("correct answer")
        break