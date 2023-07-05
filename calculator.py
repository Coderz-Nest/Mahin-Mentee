#PACE
#P -> planning,
'''
1. start of console
--Do you want to perform a calculation?: yes, no, y, n,
--If no, stop the code,

2. If yes;
--What is your First number?:
--What is your first operator?:
--What is your second number?:
--Do you want to enter a third value?:
--If no, perform calculation

3. If yes;
--What is your operator?:
--What is your third value?:

4. repeat step 3 until fifth value has been reached
--If fifth value reached, warn user that no further value can be used,
--Perform calculation

5. Ask user for another calculation,
--Do you want to perform another calculation?:
--Repeat from step 2

'''

#A -> Analyzing,
'''
def ask_user():
    values = []
    operators = []
    values_position = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
    for i, position in enemurate(values_position):
        --input from user, What is your {position} number?: 
        --input from user, What is your {position} operator?: 
        --set position boolean with default True flag
        
        while position boolean and i != 4:
            --input from the user, Do you want to enter a {values_position[i+1]} value?:
            
            if input == yes or input == y:
                set position boolean to True
                
            elif input == no or input == n:
                set position boolean to False
                
            else:
                print(User entered a wrong input)
        if position boolean is True:
            continue
        else:
            break
    return values, operators
    
def calculate(values, operators):
    result = 0
    for i, operator in enumerate(operators):
        if i == 0:
            if operator == '+':
                result += values[i] + values[i + 1]
                
            elif operator == '-':
                result += values[i] - values[i + 1]
                
            elif operator == '*':
                result += values[i] * values[i + 1]
                
            elif operator == '/':
                result += values[i] / values[i + 1]
        else:
            if operator == '+':
                result += values[i + 1]
                
            elif operator == '-':
                result -= values[i + 1]
                
            elif operator == '*':
                result *= values[i + 1]
                
            elif operator == '/':
                result /= values[i + 1]
    return result   

--set a start boolean with default false flag,

while start boolean:
    --input from the user, Do you want to perform a calculation? Yes/No, Y/N: 
    
    if input == yes or input == y:
        set start boolean to True
        values, operators = ask_user()
        result = calculate(values, operators)
        print('Your result is : ' + result)
        
    elif input == no or input == n:
        set start boolean to False
        
    else:
        print(User entered a wrong input)

'''

#C -> Construct,

def ask_user():
    ''' Asks the user for the values and operators '''
    values = []
    operators = []
    values_position = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
    for i, position in enumerate(values_position):
        num = int(input(f"What is your {position} number?: "))
        values.append(num)

        if i != 4:
            ask = input(f"Do you want to enter a {values_position[i + 1]} value?: ")
            if ask == 'yes' or ask == 'y':
                op = input(f"What is your {position} operator?:")
                operators.append(op)
                continue
            elif ask == 'no' or ask == 'n':
                break
            else:
                break
        else:
            break

    return values, operators

def calculate(values, operators):
    '''Calculates the result using the values and operators'''
    result = 0
    for i, value in enumerate(values):
        if i == 0 and len(values) > 1:
            if operators[i] == '+':
                result += values[i] + values[i + 1]

            elif operators[i] == '-':
                result += values[i] - values[i + 1]

            elif operators[i] == '*':
                result += values[i] * values[i + 1]

            elif operators[i] == '/':
                result += values[i] / values[i + 1]

        elif len(values) == 1:
            result += values[i]
            print(result)

        elif len(operators) <= 4 and i != 1:
            if operators[i-1] == '+':
                result += values[i]

            elif operators[i-1] == '-':
                result -= values[i]

            elif operators[i-1] == '*':
                result *= values[i]

            elif operators[i-1] == '/':
                result /= values[i]
    return result

while True:
    start_input = input('Do you want to perform a calculation?: ')

    if start_input == 'yes' or start_input == 'y':
        values, operators = ask_user()
        result = calculate(values, operators)
        print('Your result is : ' + str(result))

    elif start_input == 'no' or start_input == 'n':
        break

    else:
        print('User entered a wrong input(choose yes/no or y/n)')

#E -> Execute,

'''
Testing
SUCCESSFUL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
'''