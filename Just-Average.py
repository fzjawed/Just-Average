class Solution:
    def solve(self, nums, k):
        return sum(nums) - k * (len(nums) - 1) in nums