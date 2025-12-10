numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Using Set Implementation
def containsDuplicate():
    containerSet = set()

    for number in numbers:
        if number in containerSet:
            print(f"{number} is already present")
            return True
        
        containerSet.add(number)
    
    return False


# Dictionary or HashMap Implementation
def containsDuplicate():
    containerDict = dict()

    for number in numbers:
        if number in containerDict:
            print(f"{number} is already present")
            return True
        
        containerDict[number] = containerDict.get(number, 0) + 1
    
    return False

def containsDuplicate():
    numbers.sort()
    length = len(numbers) - 1

    for i in range(length):
        if numbers[i] == numbers[i+1]:
            print(f"{numbers[i]} is already present")
            return True
    
    return False

if containsDuplicate():
    print("Duplicates found")
else:
    print("No Duplicates found")