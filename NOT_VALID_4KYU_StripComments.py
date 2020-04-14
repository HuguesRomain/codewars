import re


def solution(string, markers):
    s = string
    arr1 = [s for s in re.sub(r'' + markers[0] + '(.*)\n', "@", s)]
    first__treatment = ""
    arr2 = [first__treatment for first__treatment in re.sub(
        r'' + markers[1] + '(.*)', "", s)]
    seconde__treatment = ""
    result = ""
    for elt in arr1:
        first__treatment = first__treatment + elt
    for elt in arr2:
        seconde__treatment = seconde__treatment + elt
    seconde__treatment = seconde__treatment.replace("@", "\n")

    print(seconde__treatment)
    return result


solution(
    "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
