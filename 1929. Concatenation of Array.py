class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = nums
        for i in range(len(nums)):
            out.append(nums[i])
        return out
