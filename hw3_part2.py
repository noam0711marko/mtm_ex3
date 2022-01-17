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


def check_similar(str1, str2):
    if len(str1) != len(str2):
        return False
    hist = {}
    for letter in range(26):
        hist[letter] = chr(ord('a') + letter)
    for counter in range(len(str1)):
        if str1[counter] == hist[ord(str1[counter]) - ord('a')]:
            if str2[counter] != str1[counter]:
                hist[ord(str1[counter]) - ord('a')] = str2[counter]
            else:
                hist[ord(str1[counter]) - ord('a')]=0
        else:
            if str2[counter] != hist[ord(str1[counter]) - ord('a')]:
                return False
    return True


def check_match(str):
    even = str[1:len(str):2]
    odd = str[0:len(str):2]
    if check_similar(even, odd) and check_similar(odd, even):
        return True
    return False
