#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #height of left subtree + height of right subtree
        diameter = 0
        def height(root):
            if root is None:
                return 0
            nonlocal diameter
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            diameter = max(diameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        height(root)
        return diameter
        
# @lc code=end

