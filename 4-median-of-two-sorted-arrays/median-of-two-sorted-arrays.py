class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        n=len(nums)
        if n%2!=0:
            return nums[n//2]
        else:
            return (nums[(n-1)//2]+ nums[n//2]) / 2.0