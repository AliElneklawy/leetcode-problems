def kthLargestNumber(nums, k: int) -> str:
        nums = list(map(int, nums))
        nums.sort(reverse=True)
        k-=1
        while k>=0:
            if nums.index(nums[k]) == k:
                return str(nums[k])
            k-=1
print(kthLargestNumber(["2","21","12","1"], 3))
