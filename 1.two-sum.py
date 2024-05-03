#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            
            if diff in seen:
                return [seen[diff], index]
            
            seen[num] = index
            
        return []
# @lc code=end

