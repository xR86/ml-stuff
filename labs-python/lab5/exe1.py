import sys

def operations():
    try:
        '''
        if len(sys.argv) > 1:
            for i in range(len(sys.argv)):
                print(sys.argv[i])
        '''
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(a - b)
        print(a + b)
        print(a / b)
        print(a * b)

    except ArithmeticError:
        print('Exception raised: ArithmeticError')

operations()