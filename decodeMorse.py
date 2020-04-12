def decodeMorse(morse_code):
    dict = {
        "morse letter": "letter,"
    }

    if morse_code == "":
        return "SOS"
    array__morse__code = [morse_code]
    array_morse__code_words = array__morse__code[0].split(" ")
    result = ""
    for letter in array_morse__code_words:
        if dict.get(letter) == None:
            result = result + " "
        else:
            result = result + dict.get(letter)

    result = result.strip()
    result = result.replace("  ", " ")
    return result


decodeMorse(' .... . -.--   .--- ..- -.. . ')
