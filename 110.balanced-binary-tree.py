#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced if right minus left subtree is is 1, -1 or 0
        
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left is False or right is False or abs(right - left) > 1:
                return False
            
            return 1 + max(left, right)
        
        return height(root) is not False
        
# @lc code=end

