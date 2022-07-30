def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombinations = None
    for num in numbers:
        rem = targetSum - num
        remRes = bestSum(rem, numbers)
        if remRes != None:
            remRes.append(num)
            if (shortestCombinations == None) or (len(remRes) < len(shortestCombinations)):
                shortestCombinations = remRes

    return shortestCombinations