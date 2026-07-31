# Problem Statement: Given two strings, determine if one is permutation of another or not

def permutation(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}
    for ch1, ch2 in zip(s, t):
        freq[ch1] = freq.get(ch1, 0) + 1
        freq[ch2] = freq.get(ch2, 0) - 1

    for count in freq.values():
        if count != 0:
            return False

    return True

s = "qqqa"
t = "aqqq"

if permutation(s, t):
    print("Yes, Permutation")
else:
    print("not permutation")

