from boilerplate import introduction_text


def main():
    introduction_text('7', '196 Algorithm')
    start, end = get_user_inputs()
    values = run_over_values(start, end)
    print(f'Palindrome number = {values['PAL']}\nNot Lychrel numbers = {values['NL']}\nLychrel numbers = {values['LYC']}\n')

def check_palindrome(number):
    return number == reverse_number(number)

def reverse_number(number):
    return int(str(number)[::-1])

def algo196(number):
    if check_palindrome(number):
        return "PAL"
    else:
        counter = 0
        flag = False
        newNumber = number
        while counter < 60:
            newNumber = newNumber + reverse_number(newNumber)
            if check_palindrome(newNumber):
                return "NL"
            else:
                counter += 1
        print(f'{number} is probably lychrel')
        return "LYC"

def run_over_values(start, end):
    values = {'PAL': 0, 'NL': 0, 'LYC': 0}
    for i in range(start, end + 1):
        values[algo196(i)] += 1
    return values

def get_user_inputs():
    startValue = input("\nInteger 1: ")
    endValue = input("Integer 2: ")

    try:
        startValue = int(startValue)
        endValue = int(endValue)
    except ValueError:
        startValue = 100
        endValue = 300
        print("\nPlease only input numerical values. \nValues have reverted to defaults of 100 and 300.")

    if startValue >= 1 and endValue >= startValue:
        return startValue, endValue
    else:
        return 100, 300


if __name__ == '__main__':
    main()
