def high_and_low(numbers):
    numbers = [numbers]
    numbers__array_string = numbers[0].split(" ")
    numbers__array = []
    result = ""
    for number in numbers__array_string:
        numbers__array.append(int(number))

    numbers__array = [max(numbers__array), min(numbers__array)]

    for i in numbers__array:
        result = result + str(i) + " "

    result = result.strip()
    return result


high_and_low("1 2 3 4 5")
