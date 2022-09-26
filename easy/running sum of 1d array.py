def runningSum(nums):
    sums = []
    for i in nums:
        if sums:
            sums.append(sums[-1] + i)
        else:
            sums.append(i)
    return sums
print(runningSum([1,2,3,4]))


