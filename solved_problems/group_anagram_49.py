strs = ["eat","tea","tan","ate","nat","bat"]

Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    result = {}

    for str in strs:
        key = ''.join(sorted(str))

        if key not in result:
            result[key] = []

        result[key].append(str)
    
    return list(result.values())

response = groupAnagrams(strs)
print(response)