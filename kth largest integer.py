def kthLargestNumber(nums, k: int) -> str:
        nums = list(map(int, nums))
        nums.sort(reverse=True)
        k-=1
       return str(nums[k])
print(kthLargestNumber(["2","21","12","1"], 3))
