

# Addition action
def addition():
    print('ADDITION')
    num = float(input('Enter a number: '))
    total = 0 # total numbers entered
    ans = 0 # final value after action is carried out
    while num != 0:
        ans += num
        total += 1
        num = float(input('Enter another number: '))
    return [ans, total]

# Subtraction action
def subtraction():
    print('SUBTRACTION')
    num = float(input('Enter a number: '))
    total = 0 # total numbers entered
    ans = 0 # final value after action is carried out
    while num != 0:
        ans -= num
        total += 1
        num = float(input('Enter another number: '))
    return [ans, total]

# Multiplication action
def multiply():
    print('MULTIPLICATION')
    num = float(input('Enter a number: '))
    total = 0 # total numbers entered
    ans = 0 # final value after action is carried out
    while num != 0:
        ans *= num
        total += 1
        num = float(input('Enter another number: '))
    return [ans, total]

# Average action
def average():
    average_num = []
    average_num = addition()
    total = average_num[1]
    num = average_num[0]
    ans = num/total
    return [ans, total]


def main():
    while True:
        result = []
        print(' ')
        print('SIMPLE CALCULATOR')
        print('Enter A for addition.')
        print('Enter S for subtration.')
        print('Enter M for multiplication.')
        print('Enter AV for average.')
        print('Enter Q to quit.')
        
        option = input(' ').lower()

        if option != 'q':
            if option == 'a':
                result = addition()
                print('Result = ', result[0], ', Total inputs = ', result[1])
            elif option == 's':
                result = subtraction()
                print('Result = ', result[0], ', Total inputs = ', result[1])
            elif option == 'm':
                result = multiply()
                print('Result = ', result[0], ', Total inputs = ', result[1])
            elif option == 'av':
                result = average()
                print('Result = ', result[0], ', Total inputs = ', result[1])
            else:
                print('Sorry! Invalid input.')
        else:
            break
main()