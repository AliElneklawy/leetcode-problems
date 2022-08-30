def kthLargestNumber(nums, k: int) -> str:
    nums.sort(key = int, reverse=True)
    return nums[k-1]
print(kthLargestNumber(["2","21","12","1"], 3))
