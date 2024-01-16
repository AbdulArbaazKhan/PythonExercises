# TODO: Factorial by recursive approach
# factorial(5) = 5 * factorial(4)
# factorial(n) = n * factorial(n-1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# TODO: How it will works?
# factorial(5) = 5 * factorial(4)
# factorial(5) = 5 * 4 * factorial(3)
# factorial(5) = 5 * 4 * 3 * factorial(2)
# factorial(5) = 5 * 4 * 3 * 2 * factorial(1)
# factorial(5) = 5 * 4 * 3 * 2 * 1
