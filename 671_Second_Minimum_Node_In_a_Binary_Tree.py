class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        lst = sorted(self.pre_order_traversal(root, []))
        count = 1
        for i in range(len(lst) - 1):
            if lst[i] == lst[i + 1]:
                count = count + 1
            else:
                break

        try:
            return lst[count]
        except:
            return -1

    def pre_order_traversal(self, root, ans):
        if root:
            ans.append(root.val)
        if root.left:
            self.pre_order_traversal(root.left, ans)
        if root.right:
            self.pre_order_traversal(root.right, ans)
        return ans