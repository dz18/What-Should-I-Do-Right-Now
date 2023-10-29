import random
from ast import literal_eval
from termcolor import colored

FN = 'activities.txt'

def main():
    ''''''
    print()
    data = load_data(FN)
    while True:
        inp = menu()
        print()
        if inp == 'p':
            test_fate(data)
        elif inp == 'a':
            add_option(data)
        elif inp == 'r':
            remove_option(data)
        elif inp == 'x':
            break
        elif inp == 'd':
            display_data(data)
        print()
    save_data(FN,data)

def menu():
    while True:
        sel = ('p','a','r','x','d')
        print('Test Your fate (P) | Add (A) | Remove (R) | Display Activities (D) | Exit (X)')
        inp = str(input(' >> ')).lower()
        if inp in sel:
            return inp
        print('invalid input. Try Again.')

def load_data(filename):
    with open(filename) as f:
        df = f.read()
    return literal_eval(df)

def display_data(data):
    print(f'Total Size: {len(data)}')
    print('=========================================')
    print(f'{"Activities":38}')
    print('=========================================')
    for i,k in enumerate(data):
        xCompl = str(data[k]) + 'x'
        print(f'{i + 1}. {k} {colored(xCompl, "cyan")}')

def save_data(filename, data):
    with open(filename, 'w') as f:
        f.write(str(data))

def test_fate(data):
    while True:
        fate = random.choice(list(data.items()))
        print(fate[0])
        inp = str(input('Did you complete the activity? (Y, N)\n >> ')).lower
        if inp == 'y': 
            data[fate] += 1
            break
        elif inp == 'n' : print('rolling!\n')
        else: 
            print('whatever.')
            break

def add_option(data):
    inp = input('Enter New Activity (enter \'x\' to go back):\n >> ')
    if inp == 'x' or 'X':
        return None
    print(f'\nYou\'ve entered, \"{inp}\", to the activities list.\n')
    data.append(inp)    
    save_data(FN, data)

def remove_option(data):
    print("Enter the number of the activity you wish to remove.")
    temp = list()
    for i,k in enumerate(data):
        temp.append(k)
        xCompl = str(data[k]) + 'x'
        print(f'{i + 1}. {k} {colored(xCompl, "cyan")}')

    inp = int(input(" >> "))
    del data[temp[inp - 1]]
    save_data(FN, data)

main()

