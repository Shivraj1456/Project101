import random

min_val=1
max_val=6


roll_again = "y"

while roll_again=="yes" or roll_again=='y':
    print('rolling the dice....')
    print('your value are....')
    
    print(random.randint(min_val,max_val))
    
    roll_again = input("write yes to role again")