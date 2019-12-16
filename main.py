def calc(*args, **kwargs):

    num = float(input('Enter number of elements: '))
    e = 0
    a = float(input('Enter element: '))
    op = input('Enter operation: ')
    b = float(input('Enter element: '))
    result = 0
    if op == "+":
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '/':
        if b == 0:
            print('Error 2 element cant be zero')
        else:
            result = a / b
    elif op == '*':
        result = a * b

    if num > 2:

        while e < num-2:

            op = input('Enter operation: ')
            b = float(input('Enter element: '))
            e += 1

            if op == "+":
                result = result + b
            elif op == '-':
                result = result - b
            elif op == '/':
                if b == 0:
                    print('Error 2 element cant be zero')
                else:
                    result = result / b
            elif op == '*':
                result = result * b
    return result


print(calc())