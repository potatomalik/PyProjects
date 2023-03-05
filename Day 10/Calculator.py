def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

a=float(input('Enter a number: '))
while True:
    op=input('''Choose an operation
                +
                -
                *
                /
                ''')
    b=float(input('Enter next number: '))


    match op:
        case '+':
            c=add(a,b)
        case '-':
            c=substract(a,b)
        case '*':
            c=multiply(a,b)
        case '/':
            c=divide(a,b)
        case _:
            print('INVALID')
    print(c)
    
    choice=input(f"Type 'Y' to continue operation with {c},\n'O' for calculations with other number,\n 'N' to stop.").lower()
    if choice=='y':
        a=c
    elif choice=='o':
        a=float(input('Enter a number: '))
    else:
        break