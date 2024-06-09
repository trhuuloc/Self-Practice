import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def elu(x, alpha=0.01):
    return alpha * (math.exp(x) - 1) if x <= 0 else x

def apply_activation_function():
    x = input('Enter a value for x: ')
    if not is_number(x):
        print('The input must be a number.')
        return

    x = float(x)
    activation_function = input('Choose an activation function (sigmoid, relu, elu): ')

    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f'The function "{activation_function}" is not supported.')
        return

    if activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'elu':
        result = elu(x)

    print(f'{activation_function}: f({x}) = {result}')

apply_activation_function()
