#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        
        for i in s:
            if i in s:
                count_s[i] += 1
        
        for i in t:
            if i in t:
                count_t[i] += 1
                
        return (count_s == count_t)
        
# @lc code=end

