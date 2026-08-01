# https://www.hackerearth.com/problem/algorithm/palindrome-check-2-1/
# Read Cracking the coding interview book's array strings section if needed for the problem desciption

def is_palindrome_permutation(pharse: str) -> bool:
    if len(pharse) == 0:
        return True

    pharse = pharse.lower()
    frequency = {}

    for ch in pharse:
        if ch >= 'a' and ch <= 'z':
            frequency[ch] = frequency.get(ch, 0) + 1

    found_odd = False
    for _, v in frequency.items():
        if v % 2 == 1:
            if found_odd == True:
                return False
            else:
                found_odd = True  
            
    return True

pharse = "Tact Coa"
if is_palindrome_permutation(pharse):
    print("It's a palindrome")
else:
    print("Not palindrome") 