class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for i in range(len(nums)//2):
            out.append(nums[:n][i])
            out.append(nums[n:][i])
        return out
