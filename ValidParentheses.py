
open__parenthese = ["("]
close__parenthese = [")"]


def valid_parentheses(string):
    result = []
    for elt in string:
        if elt in open__parenthese:
            result.append(elt)
            print(result)
        elif elt in close__parenthese:
            close__index = close__parenthese.index(elt)
            if (len(result) > 0 and open__parenthese[close__index] == result[len(result)-1]):
                result.pop()
            else:
                return False
    if len(result) != 0:
        return False
    else:
        return True


valid_parentheses("iwduo(md)oivdbcuz(()mcvupp")
