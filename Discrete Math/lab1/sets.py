

def var():
    g = 21
    n = 8
    m = "ІО"
    if m == "ІО": n += 2
    var = (n + g % 60) % 30 + 1
    return f"Oksuzova T. E.\n" \
           f"My group: {m}-z{g}\n" \
           f"My number in group: {n-2}\n" \
           f"My variant: {var}"


def union_set(set1, set2):
    a_set = list(set1)
    b_set = list(set2)
    [a_set.append(item) for item in b_set if item not in a_set]
    return set(a_set)


def intersection_set(set1, set2):
    a_set = list(set1)
    b_set = list(set2)
    c_set = []
    [c_set.append(item) for item in b_set if item in a_set]
    return set(c_set)


def difference_set(set1, set2):
    a_set = list(set1)
    b_set = list(set2)
    c_set = []
    [c_set.append(item) for item in a_set if item not in b_set]
    return set(c_set)


def settostr(set):
    return " ".join(map(str, set))




# print(difference_set((1), (1)))
#
# a = {1}
# b = {1}
# print(a.difference(b))