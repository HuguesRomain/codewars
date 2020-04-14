def pig_it(text):
    text__array = []
    text__array = text.split(" ")
    result = ""
    for word in text__array:
        letter = ""
        letter = word[:1]
        if letter == "?" or letter == "!" or letter == ",":
            result = result + word[1:] + letter + " "
        else:
            result = result + word[1:] + letter + "ay" + " "

    result = result.strip()

    print(result)
    return result


pig_it("salut les amis !")
