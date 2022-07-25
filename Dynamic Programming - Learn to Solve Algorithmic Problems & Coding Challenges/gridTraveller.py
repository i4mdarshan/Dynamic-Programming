# No. of ways to travel a given grid using x,y co-ordinates. The traveller should start from the top-left of the grid to the bottom-right as the END position. You can travel only in downward or right in the grid to reach the END
# Eg gridTraveller(1,1) -> 0 ways as their is no way to travel in the grid
# Eg gridTraveller(3,3) -> 3 ways

# Step 1: Break the problem into subparts and write the base cases where the ans remains fixed

#  _ -> (0,0) -> 0 ways
#  _ -> (0,2) -> 0 ways
#  _ -> (2,0) -> 0 ways
# The above cases will have 0 ways since their is no possibility of making a grid even if any of X or Y is 0


# For 1 x 1 grid
#  # -> (1,1) -> 1 way

# Step 2: Find the co-ordinates changing pattern.
# For 3 x 3 grid
# x denotes rows and y denotes columns
#    M##   -> M is at (0,0)
#    ###
#    ###

#    ###   -> M is at (1,0)
#    M##
#    ###

#    ###   -> M is at (2,0)
#    ###
#    M##

#    ###   -> M is at (2,1)
#    ###
#    #M#

#    ###   -> M is at (2,3) : total -> 6 ways
#    ###
#    ##M

def gridTraveller(x,y, memo = {}):
    # Store the keys as unique ID so we introduced comma seperator
    key = str(x) + ',' + str(y)
    # check if the x,y combination exists in the memo from the previous if yes then return the calculation ans 
    if key in memo: return memo[key]
    if (x == 1 and y == 1): return 1
    if (x == 0 or y == 0): return 0

    # store the calculation inside memo
    memo[key] = gridTraveller(x - 1,y) + gridTraveller(x,y - 1)

    return memo[key]

print(gridTraveller(18,18))