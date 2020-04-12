def sum_two_smallest_numbers(numbers):
    first_low = " "
    seconde_low = " "

    first_low = min(numbers)
    numbers.remove(first_low)

    seconde_low = min(numbers)
    numbers.remove(seconde_low)

    return first_low + seconde_low


sum_two_smallest_numbers([5, 8, 12, 18, 22])
