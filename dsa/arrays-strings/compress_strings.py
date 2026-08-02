def compress(s: str) -> str:
    result = []
    count = 0
    n = len(s)
    
    for i in range(n):
        count += 1
        if i + 1 == n or s[i] != s[i + 1]:
            result.append(s[i])
            result.append(str(count))
            count = 0
    
    result = ''.join(result)
    
    return result if len(result) < len(s) else s

s = "aab"
result = compress(s)
print(result)

