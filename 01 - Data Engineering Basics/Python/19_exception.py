#exception
def divide(a,b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Dividing by Zero.")
        finally:
            print("In finally clause.")

if __name__ == '__main__':
    try:
        a = pow(2, 4)
        print("Value of 'a' :", a)
        b = pow(2, 'hello')  # results in exception
        print("Value of 'b' :", b)
    except TypeError as e:
        print('oops!!!')
    print('Out of try ... except.')

    try:
        a = 2;
        b = 'hello'
        if not (isinstance(a, int)
                and isinstance(b, int)):
            raise TypeError('Two inputs must be integers.')
        c = a ** b
        print(c)
    except TypeError as e:
        print(e)
    print('First call')
    print(divide(14, 7))
    print('Second call')
    print(divide(14, 0))