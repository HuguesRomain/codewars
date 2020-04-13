def create_phone_number(n):
    i = 0
    first__part = ""
    second__part = ""
    third__part = ""
    result = ""
    while i < len(n):
        if i <= 2:
            first__part = first__part + str(n[i])

        elif i <= 5:
            second__part = second__part + str(n[i])

        else:
            third__part = third__part + str(n[i])

        i = i + 1

    first__part = "(" + first__part + ")"
    second__part = " " + second__part + "-"
    result = first__part + second__part + third__part

    print(result)
    return result


create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
