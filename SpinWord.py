def spin_words(sentence):
    array = []
    result = ""
    for i in sentence:
        array = sentence.split(" ")

    for word in array:
        if len(word) < 5:
            result = result + word + " "
        elif len(word) >= 5:
            stringlength = len(word)
            result = result + word[stringlength::-1] + " "

    result = result.strip()
    return result


spin_words("Welcome to the jungle")
