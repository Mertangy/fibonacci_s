"""Fibonacci series"""


# define a fibonacci series up to integer n
def fibonacci(n):
    """Generate a fibonacci series up to and including integer N"""
    first, second = 0, 1
    fib = [first, second]
    for i in range(2, n + 1):
        next_num = first + second
        fib.append(next_num)
        first = second
        second = next_num
        i += 1
    return fib


# get number from user and check if its a fibonacci number
while True:
    user_input = input("Enter a number to check,Q to quit: ")
    try:
        number = int(user_input)
        if number in fibonacci(number):
            print(f"{number} is a fibonacci number.")
        else:
            print(f"{number} is not a fibonacci number")
    except ValueError:
        if user_input.lower() == 'q':
            print("You have Chosen to quit")
            break
        print("Please enter a positive integer")
