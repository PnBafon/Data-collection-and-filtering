current_amount = float(input('Enter amount in USD: \n'))
currency_code = input("Enter The Currency Code: \n")

# performing the conversion
def convert_currency(amount, code):
    currency_and_code = {
        'EUR': 0.9203,
        'CFA': 602.61,
        'NGN': 774.56
    }
    try:
        # calculating the exchange amount
        amount = currency_and_code[code] * amount
        converted_amount = f"{amount} {code }"
        return converted_amount
    except:
        print('Currency code not supported')


amount = convert_currency(current_amount,currency_code)

print(f"{current_amount}USD in {currency_code} is: \n {amount}")