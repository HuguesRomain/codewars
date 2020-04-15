from collections import Counter


def scramble(s1, s2):
    if len(s1) < len(s2):
        return False
    str1 = Counter(s1)
    str2 = Counter(s2)
    print(str1)
    print(str2)
    for x in range(len(s2)):
        if str1[s2[x]] < str2[s2[x]]:
            return False
    return True


scramble('dblzhtwftwoav', 'lvttwwfbzaohd')
