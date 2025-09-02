# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs_in_order(node):
            if not node:
                return False

            if dfs_in_order(node.left): return True

            if k - node.val in seen:
                return True
            seen.add(node.val)

            if dfs_in_order(node.right): return True

            return False

        return dfs_in_order(root)
