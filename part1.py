def add_product(line, matamikya):
    name = line[1]
    price = float(line[2])
    amount = float(line[3])
    if name in matamikya or price < 0 or amount < 0:
        return matamikya
    matamikya[name] = [price, amount, 0]
    return matamikya


def change_amount(line, matamikya):
    name = line[1]
    amount_to_add = float(line[2])
    if name not in matamikya:
        return matamikya
    matamikya[name][1] += amount_to_add
    return matamikya


def ship_order(line, matamikya):
    index = 0
    while index < len(line):
        name = line[index + 1]
        amount = float(line[index + 2])
        if name not in matamikya or amount > matamikya[name][1]:
            index += 3
            continue
        matamikya[name][1] -= amount
        matamikya[name][2] += matamikya[name][0]*amount   # possible error
        index += 3  # magic number
    return matamikya


def file_to_list(input_file):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    counter = 0
    for line in lines:
        line = line.replace(",", "")
        line = line.split()
        del line[1]
        lines[counter] = line
        counter += 1
    return lines


def file_to_matamikya(file_name):
    matamikya = {}
    new_list = file_to_list(file_name)
    for line in new_list:
        if line[0] == "add":
            matamikya = add_product(line, matamikya)
        elif line[0] == "change":
            matamikya = change_amount(line, matamikya)
        elif line[0] == "ship":
            matamikya = ship_order(line, matamikya)
    matamikya = dict(sorted(matamikya.items(), key=lambda x: x[0]))
    return matamikya


def find_best_selling_product(file_name):
    matamikya = file_to_matamikya(file_name)
    current_best = ("", 0)
    for k, v in matamikya.items():
        if v[2] > current_best[1]:
            current_best = (k, v[2])
    return current_best


def find_k_most_expensive_products(file_name, k):
    matamikya = file_to_matamikya(file_name)
    expensive = []
    for curr_key, val in matamikya.items():
        expensive.append((curr_key, val[0]))
        expensive = sorted(expensive, key=lambda x: x[1], reverse=True)
        if len(expensive) > k:
            del expensive[len(expensive)-1]
    for i in range(len(expensive)):
        expensive[i] = expensive[i][0]
    return expensive
