# Brute Force
# def bestSum(targetSum, numbers):
#     if targetSum == 0:
#         return []

#     if targetSum < 0:
#         return None

#     shortestCombinations = None
#     for num in numbers:
#         rem = targetSum - num
#         remRes = bestSum(rem, numbers)
#         if remRes != None:
#             remRes.append(num)
#             if (shortestCombinations == None) or (len(remRes) < len(shortestCombinations)):
#                 shortestCombinations = remRes

#     # print(shortestCombinations)
#     return shortestCombinations


# memoized solution
def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        rem = targetSum - num
        remRes = bestSum(rem, numbers,memo)
        if remRes != None:
            # Changing "shortest_combination = remainder_combination" to "shortest_combination = remainder_combination.copy()". Memory allocation seems to work a little differently in Javascript, but in Python shortest_combination and remainder_combination are both pointing to the same list in memory, causing this error.
            # Edit: Also, since there still appears to be bugs when using different inputs, change"remainder_combination.append(num)" to a copy before appending num e.g. r_c = remainder_combination.copy(), r_c.append(num), and compare this list against shortest_combination as opposed to the original.
            remResult = remRes.copy() 
            remResult.append(num)
            if (shortestCombination == None) or (len(remResult) < len(shortestCombination)):
                shortestCombination = remResult.copy()

    memo[targetSum] = shortestCombination
    return shortestCombination

# print(bestSum(7, [5,3,4,7]))
# print(bestSum(8, [2,3,5]))
print(bestSum(100, [1,2,5,25]))