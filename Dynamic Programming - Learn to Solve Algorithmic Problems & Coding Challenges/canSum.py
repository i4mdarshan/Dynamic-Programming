# Find if the numbers present in the list given can generate the targetSum
# NOTE: The numbers in the list can be REUSED to generate the targetSum

# Brute force solution
# def canSum(targetSum, numbers):
#     if (targetSum == 0):
#         return True
#     if (targetSum < 0):
#         return False;

#     for num in numbers:
#         rem = targetSum - num
#         if (canSum(rem,numbers) == True):
#             return True
#     return False

# Memoization Solution
def canSum(targetSum, numbers, memo ={}):
    # print(memo)
    if targetSum in memo:
        return memo[targetSum] 
    if (targetSum == 0):
        return True
    if (targetSum < 0):
        return False;

    for num in numbers:
        rem = targetSum - num
        if (canSum(rem,numbers,memo) == True):
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False



# print(canSum(7,[2,3]))
# print(canSum(7,[5,3,4,7]))
# print(canSum(7,[2,4]))
# print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))
