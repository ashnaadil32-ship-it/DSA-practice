# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Shift the existing bits left and add the current node's bit
            current_sum = (current_sum << 1) | node.val
            
            # If it's a leaf node, return the completed binary value
            if not node.left and not node.right:
                return current_sum
            
            # Sum up paths from both left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
        return dfs(root, 0)