def check_palindrom(str, k):
    if k == 1 or k == 0:
        return True
    if k > len(str):
        return False
    else:
        if str[0] != str[k - 1]:
            return False
    return check_palindrom(str[1: k - 1], k - 2)


def get_palindrom_dict(str):
    res = {}
    for k in range(len(str)):
        palindroms = []
        for index in range(len(str)):
            if check_palindrom(str[index:], k + 1):
                palindroms.append(str[index:index + k + 1])
        if len(palindroms) > 0:
            res[k + 1] = palindroms
    return res


def check_similar(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if i != str1.find(str1[i]):
            if str2[i] != str2[str1.find(str1[i])]:
                return False
    return True


def check_match(str):
    even = str[1:len(str):2]
    odd = str[0:len(str):2]
    if check_similar(odd, even):
        return True
    return False
