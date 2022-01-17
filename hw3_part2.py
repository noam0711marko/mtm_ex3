def check_palindrom(str, k):
    if k == 1 or k == 0:
        return True
    if k > len(str):
        return False
    else:
        if str[0] != str[k - 1]:
            return False
    return check_palindrom(str[1: k - 1], k - 2)


def get_palindromic_dict(str):
    res = {}
    for k in range(len(str)):
        palindroms = []
        for index in range(len(str)):
            if check_palindrom(str[index:], k + 1):
                palindroms.append(str[index:index + k + 1])
        if len(palindroms) > 0:
            res[k + 1] = palindroms
    return res


def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield char


def check_match(str):
    hist1 = {}
    hist2 = {}
    for letter in character_range('a', 'z'):
        hist1[letter] = -1
        hist2[letter] = -1
