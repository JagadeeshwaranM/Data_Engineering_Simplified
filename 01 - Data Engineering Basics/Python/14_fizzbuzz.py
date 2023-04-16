#fizzbuzz module
def fizzBuzz(n):
    # Write your code here
    for fizzBuzz in range(1,n+1):
        if fizzBuzz % 15 == 0:
            print('FizzBuzz')
            continue
        elif fizzBuzz % 3 ==0:
            print('Fizz')
            continue
        elif fizzBuzz % 5 == 0:
            print('Buzz')
            continue
        print(fizzBuzz)

if __name__ == '__main__':
    x = int(input("Enter number for range"))
    fizzBuzz(x)