#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingParentheses = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack[-1] != matchingParentheses[char]:
                    return False
                stack.pop()
        if not stack:
            return True
# @lc code=end

