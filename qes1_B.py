def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a non-negative number: "))

try:
    result = factorial(number)
    print("The factorial of {} is {}".format(number, result))
except ValueError as e:
    print("Error: {}".format(e))
