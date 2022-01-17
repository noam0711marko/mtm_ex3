def add_product(line, matamikya):
    name = line[1]
    price = int(line[2])
    amount = int(line[3])
    if name in matamikya or price < 0 or amount < 0:
        return matamikya
    matamikya[name] = (price, amount, 0)
    return matamikya


def change_amount(line, matamikya):
    name = line[1]
    amount_to_add = int(line[2])
    if name not in matamikya:
        return matamikya
    matamikya[name][1] += amount_to_add
    return matamikya


def ship_order(line, matamikya):
    index = 0
    while index < len(line):
        name = line[index + 1]
        amount = line[index + 2]
        if name not in matamikya or amount > matamikya[name][1]:
            continue
        matamikya[name][1] -= amount
        matamikya[name][2] += matamikya[name][0] * amount
        index += 3  # magic number
    return matamikya


def file_to_list(input_file):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split()
        del line[1]
    return lines


def file_to_matamikya(file_name):
    matamikya = {}
    new_list = file_to_list(file_name)
    for line in new_list:
        if line[1] is "add":
            matamikya = add_product(line, matamikya)
        elif line[1] is "change":
            matamikya = change_amount(line, matamikya)
        else:
            matamikya = ship_order(line, matamikya)
    return matamikya


def find_best_selling_product(file_name):
    matamikya = file_to_matamikya(file_name)
    current_best = ("", 0)
    for k, v in matamikya.items():
        if v[3] > current_best[1]:
            current_best = (k, v[3])
    return current_best


def sort_by_2nd_in_tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if tup[j][1] > tup[j + 1][1]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


def find_k_most_expensive_products(file_name, k):
    matamikya = file_to_matamikya(file_name)
    expensive = []
    for curr_key, val in matamikya.items():
        expensive.append((curr_key, val[0]))
        if len(expensive) > k:
            expensive = sorted(expensive, key=lambda x: x[1], reverse=True)
            del expensive[len(expensive)-1]
    return expensive
