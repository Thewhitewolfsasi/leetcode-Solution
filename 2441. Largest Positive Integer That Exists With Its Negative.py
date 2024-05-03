"""Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.

Example 1:
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
"""
#Brute Force
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos = set()
        neg = set()
        for i in nums:
            if i > 0:
                pos.add(i)
            else:
                neg.add(abs(i))
        inter = list(pos & neg)
        inter.sort()
        if len(inter) == 0:
            return -1
        else:
            return inter[-1]
