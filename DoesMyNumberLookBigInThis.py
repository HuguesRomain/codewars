def narcissistic(value):
    numbers = str(value)
    second_calc = []
    result = 0
    for number in numbers:
        print(len(numbers))
        second_calc.append(int(number) ** len(numbers))

    result = sum(second_calc)

    if result == int(numbers):
        return True
    else:
        return False


narcissistic(371)
