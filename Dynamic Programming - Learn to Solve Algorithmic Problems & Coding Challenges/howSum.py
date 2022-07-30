# Given a list of the numbers print anyone combination of the given targetSum 
# You can use the number as many times as you want
# If their is no possible combination return null


# Brute Force Solution
# def howSum(targetSum, numbers):
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None
    
#     for num in numbers:
#         rem = targetSum - num
#         remRes = howSum(rem,numbers)
#         if remRes != None:
#             remRes.append(num)
#             return remRes

#     return None
# let m be len of numbers
# let n be the target Sum
# Time: O(m*m^n)
# Space: O(m)


# Momized Solution
def howSum(targetSum, numbers, memo ={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        rem = targetSum - num
        remRes = howSum(rem,numbers)
        if remRes != None:
            remRes.append(num)
            memo[targetSum] = remRes
            return memo[targetSum]

    memo[targetSum] = None
    return None




# print(howSum(7,[2,3])) #-> [2,2,3]
# print(howSum(7,[2,4]))
# print(howSum(8,[2,3,5]))
# print(howSum(300, [7,14])) 