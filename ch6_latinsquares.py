from boilerplate import introduction_text

def main():
    introduction_text('6', 'Latin Squares')
    order, topleft = get_user_inputs()

    for x in range(0, order):
        print(" ".join(generate_row(topleft + x, order)))

def generate_row(startValue, order):
    if startValue > order:
        startValue -= order

    myList = [str(x) for x in range(startValue, order + 1)]
    for x in range(1, startValue):
        myList.append(str(x))
    return myList

def get_user_inputs():
    order = input("Please input the order of square: ")
    topleft = input("Please input the top left number: ")

    try:
        order = int(order)
        topleft = int(topleft)
    except ValueError:
        order = 5
        topleft = 3
        print("\nPlease only input numerical values. \nValues have reverted to defaults of order of 5 and top left number of 3.")

    if order >= 1 and topleft <= order and topleft >= 1:
        return order, topleft
    else:
        return 5, 3


if __name__ == "__main__":
    main()