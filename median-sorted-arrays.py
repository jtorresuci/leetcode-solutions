class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        div = len(nums) // 2
        is_odd = len(nums)%2

        if is_odd:
            return nums[div]
        else:
            return (nums[div-1] + nums[div]) / 2