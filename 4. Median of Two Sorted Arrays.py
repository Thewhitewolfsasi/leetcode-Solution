class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        indx = len(arr)//2
        if len(arr)%2 == 0:
            median = (arr[indx-1] + arr[indx])/2
        else:
            median = arr[indx]
        return median
