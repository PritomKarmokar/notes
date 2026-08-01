# https://algo.monster/liteproblems/161
# Currently it's very bad solution version for the problem statement. Need to optimize it properly
def is_one_edit_distance(s: str, t: str) -> bool:
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

s = "ab"
t = "ad"

if is_one_edit_distance(s, t):
    print("Yes")
else:
    print("No")