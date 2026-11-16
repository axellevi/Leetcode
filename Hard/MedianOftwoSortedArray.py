class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lists = sorted(nums1 + nums2)
        n = len(lists)
        if len(lists) % 2 == 0:
            mid1 = lists[(n // 2) - 1]
            mid2 = lists[n // 2]
            return (mid1 + mid2 )/ 2.0
        else:
            mid = float(lists[n // 2])
            return mid