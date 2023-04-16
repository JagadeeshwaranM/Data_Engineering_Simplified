#calculator
import operation
import math


# def cls():
#    print "\n"*100

def main_menu_dis():
    #    cls()
    print('#' * 100)
    print('############ CALCULATOR######################')
    print('#' * 100)
    print('          1. Simple calc                     ')
    print('          2. sci calc                        ')
    print('          3. exit                            ')
    print("Enter your Choice")
    num = int(input())
    menu_choice(num)


def menu_choice(num ):
    print(num)
    if(num == 1):
        print('simple')
        simple_calc_menu()
        num2 = int(input("Enter option for simple calculator"))
        sim_calc_menu_choice(num2)
    elif(num == 2):
        sci_calc_menu()
        num2 = int(input("Enter option for scientific calculator"))
        sci_calc_menu_choice(num2)
    else:
        print('invalid')


def simple_calc_menu():

    print('             Simple calc                     ')
    print('          1. ADD                             ')
    print('          2. SUB                             ')
    print('          3. MUL                             ')
    print('          4. DIV                             ')
    print('          5. GO BACK                         ')
    print("Enter your Choice")


def sci_calc_menu():
    print('             Scientific Calculator           ')
    print('          1. sin                             ')
    print('          2. cos                             ')
    print('          3. power of                        ')
    print('          4. square root                     ')
    print('          5. GO BACK                         ')
    print("Enter your Choice")


# -----------------------------------------------------------------------------------------------

def sim_calc_menu_choice(num2):
    if num2 == 1:
        print("Enter two Numbers to be added:")
        a = int(input())
        b = int(input())
        operation.my_add(a, b)
        print("Sum of two numbers is:", operation.my_add(a, b))
        print("Press any key to continue")
        num3 = int(input())
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 2:
        print("Enter two Numbers to be subtracted:")
        a = int(input())
        b = int(input())
        operation.my_sub(a, b)
        print("difference of two numbers is:", operation.my_sub(a, b))
        print("Press any key to continue")
        num3 = int(input())
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 3:
        print("Enter two Numbers to be multiplyed:")
        a = int(input())
        b = int(input())
        operation.my_mul(a, b)
        print("Result of multiplication of two numbers is:", operation.my_mul(a, b))
        num3 = int(input())
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 4:
        print("Enter two Numbers to be divided:")
        a = int(input())
        b = int(input())
        operation.my_div(a, b)
        print("Result of division of two numbers is:", operation.my_div(a, b))
        num3 = int(input())
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 5:
        main_menu_dis()
    else:
        print('Invalid Choice')


def sci_calc_menu_choice(num2):
    if num2 == 1:
        print("Enter degree:")
        a = int(input())
        operation.my_sin(a)
        print("Sin Value is :", operation.my_sin(a))
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 2:
        print("Enter degree:")
        a = int(input())
        operation.my_cos(a)
        print("cos Value is :", operation.my_cos(a))
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 3:
        print("Enter two number to calculate power:")
        a = int(input())
        b = int(input())
        operation.my_pow(a, b)
        print("power of two  Value is :", operation.my_pow(a, b))
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 4:
        print("Enter number to which square root needs to be calculated:")
        a = int(input())
        operation.my_sqrt(a)
        print("power of two  Value is :", operation.my_sqrt(a))
        simple_calc_menu()
        num2 = int(input())
        sim_calc_menu_choice(num2)
    elif num2 == 5:
        main_menu_dis()
    else:
        print('Invalid Choice')


main_menu_dis()



