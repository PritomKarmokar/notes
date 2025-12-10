s = "anagram"
t = "nagaram"

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    length = len(s)
    freq = dict()

    for i in range(length):
        freq[s[i]] = freq.get(s[i], 0) + 1
        freq[t[i]] = freq.get(t[i], 0) - 1

    for key, val in freq.items():
        if val != 0:
            return False    
    
    return True