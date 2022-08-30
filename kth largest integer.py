def kthLargestNumber(nums, k: int) -> str:
        nums.sort(key = int, reverse=True)
        k-=1
       return nums[k]
print(kthLargestNumber(["2","21","12","1"], 3))
