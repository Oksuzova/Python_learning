while True:
    try:
        price = float(input('Enter your price:'))
        if price >= 0:
            print('tax = 18%')
            tax = price * 0.18
            print(f'tax = {tax}')
            print('tip = 10%')
            tip = price * 0.10
            print(f'tip = {tip}')
            full_price = price + tax + tip
            print(f'Full = {full_price}')
            break
        else:
            print('Error')
    except ValueError:
        print('Please,enter your price')

