# https://algo.monster/liteproblems/161
# Currently it's very bad solution version for the problem statement. Need to optimize it properly
def is_one_edit_distance_v1(s: str, t: str) -> bool:
    if len(s) == len(t):
        replaceFound = False
        for a, b in zip(s, t):
            if a != b:
                if replaceFound is True:
                    return False
                replaceFound = True
        return replaceFound
    else:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            freq[ch] = freq.get(ch, 0) - 1

        counter = 0
        for _, v in freq.items():
            if v != 0:
                counter += 1

        return counter == 1

def is_one_edit_distance(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    if len(s) == len(t):
        return one_edit_replace(s, t)
    elif len(s) + 1 == len(t):
        return one_edit_insert(s, t)
    elif len(s) - 1 == len(t):
        return one_edit_insert(t, s)

    return False

def one_edit_replace(s: str, t: str) -> bool:
    counter = 0
    for ch1, ch2 in zip(s, t):
        if ch1 != ch2:
            counter += 1

    return counter == 1

def one_edit_insert(s: str, t: str) -> bool:
    index1, index2 = 0, 0
    l1 = len(s)
    l2 = len(t)
    while index2 < l2 and index1 < l1:
        if s[index1] != t[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1 
    return True

s = "ab"
t = "ad"

if is_one_edit_distance(s, t):
    print("Yes")
else:
    print("No")