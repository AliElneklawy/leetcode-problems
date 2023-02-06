def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and len(nums2) == 1:
            return nums2[0]
        
        elif len(nums1) == 1 and not nums2:
            return nums1[0]
    
        merged = sorted(nums1 + nums2)
        length = len(merged)
    
        if length % 2 != 0:
            mid = merged[int((1 + length) / 2) - 1]
            return mid
      
        mid1 = merged[int(length / 2)]
        mid2 = merged[int(length / 2) - 1]
        return (mid1 + mid2) / 2