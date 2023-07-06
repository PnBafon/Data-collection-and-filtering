
numbers = []
even_numbers = []
number = ''
print('Enter numbers, and press q to quit')

number = input()
while number != 'q':
    try:
        numbers.append(int(number))
    except:
        print('please enter a number and q to quite execution')
    number = input()


def filter_even_numbers(numbers):
    for number in numbers:
        if (number % 2) == 0:
            even_numbers.append(number)
    return even_numbers

# invoking the function
all_even_numbers = filter_even_numbers(numbers)

print(all_even_numbers)
