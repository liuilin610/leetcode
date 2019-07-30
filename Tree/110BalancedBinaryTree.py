# 110 Balanced Binary Tree

class solution(object):
    def BalancedBinaryTree(self, root):
        """
        : type root: TreeNode
        : rtype : bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root: return 0
            left, right = self.dfs(root.left), self.dfs(root.right)
        if left < 0 or right < 0 or abs(left-right) > 1 :
            return -1
        return max(left, right) + 1
            