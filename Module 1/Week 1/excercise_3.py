import random

def is_number(n):
    try:
        float(n)
    except ValueError:
        print('The number of samples must be an integer.')
        return False
    return True

def loss_function():
    n = (input('Input number of samples (interger number) which are generated: '))
    if not is_number(n):
        return

    n = int(n)
    loss_name = input('Input loss name:')

    if loss_name in ['MAE', 'MSE', 'RMSE']:
        if loss_name == 'MAE':
            total_loss = 0.0
            for i in range(n):
                y = random.uniform(0, 10)
                y_hat = random.uniform(0, 10)
                loss = abs(y - y_hat)
                total_loss += loss
                print(f'loss name: MAE, sample: {i}, pred: {y_hat}, target: {y}, loss: {loss}')
            print(f'final MAE: {total_loss / n}')

        elif loss_name == 'MSE':
            total_loss = 0.0
            for i in range(n):
                y = random.uniform(0, 10)
                y_hat = random.uniform(0, 10)
                loss = (y - y_hat) ** 2
                total_loss += loss
                print(f'loss name: MSE, sample: {i}, pred: {y_hat}, target: {y}, loss: {loss}')
            print(f'final MSE: {total_loss / n}')

        elif loss_name == 'RMSE':
            total_loss = 0.0
            for i in range(n):
                y = random.uniform(0, 10)
                y_hat = random.uniform(0, 10)
                loss = (y - y_hat) ** 2
                total_loss += loss
                print(f'loss name: RMSE, sample: {i}, pred: {y_hat}, target: {y}, loss: {loss}')
            print(f'final RMSE: {(total_loss / n) ** 0.5}')

    else:
        print('The loss function name must be one of the following: MAE, MSE, RMSE.')

loss_function()
