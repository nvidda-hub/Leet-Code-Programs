# 1. If both trees are empty then we return empty.
# 2. Otherwise, we will return a tree. The root value will be t1.val + t2.val,
# except these values are 0 if the tree is empty.
# 3. The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
# 4. The right child is similar.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        ans.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
        return ans
