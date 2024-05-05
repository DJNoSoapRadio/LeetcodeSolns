#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredS = ''
        for char in s:
            if char.isalnum():
                filteredS += char.lower()
            
        start = 0
        end = len(filteredS) - 1
        
        while (start < end):
            if (filteredS[start] != filteredS[end]):
                return False
            start += 1
            end -= 1
        
        return True
        
        
# @lc code=end

