def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def is_number(n):
    try:
        int(n)
        if n <= 0:
            raise ValueError
    except ValueError:
        print('number of samples must be an integer number and greater than 0')
        return False
    return True

def approx_sin(x, n):
    if not is_number(n):
        return
    sum = 0.0
    for i in range(n + 1):
        sum += ((-1) ** i * (x) ** (2 * i + 1) / factorial(2 * i + 1))
    print(sum)

def approx_cos(x, n):
    if not is_number(n):
        return
    sum = 0.0
    for i in range(n + 1):
        sum += ((-1) ** i * (x) ** (2 * i) / factorial(2 * i))
    print(sum)

def approx_sinh(x, n):
    if not is_number(n):
        return
    sum = 0.0
    for i in range(n + 1):
        sum += ((x) ** (2 * i + 1) / factorial(2 * i + 1))
    print(sum)

def approx_cosh(x, n):
    if not is_number(n):
        return
    sum = 0.0
    for i in range(n + 1):
        sum += ((x) ** (2 * i) / factorial(2 * i))
    print(sum)

approx_sin(3.14, 10)
approx_cos(3.14, 10)
approx_sinh(3.14, 10)
approx_cosh(3.14, 10)
