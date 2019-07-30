# 98 Validate Binary Search Tree

# I-DFS
class Solution(object):
    def ValidateBST(self, root):
        """
        : type root : TreeNode
        : rtype : bool
        """
        pre = [None]
        return self.dfs(root, pre)

    def dfs(self, root, pre):
        if not root: return True
        if not self.dfs(root.left, pre) or pre[0] and root.val <= pre[0].val:
            return False
        pre[0]= rootreturn self.dfs(root.right, pre)

# recursive
class Solution1(object):
    def ValidateBST1(self, root):
        """
        : type root : TreeNode
        : rtype : bool
        """
        INF = float('inf')
        return self.judge(root, -INF, INF)
    def judge(self, root, minV, maxV):
        if not root: return True
        if root.val <= minV or root.val => maxV: return False
        return self.judge(root.left, minV, root.val) and self.judge(root.right, root.val, maxV)

# III -BFS
class Solution3(object):
    def ValidateBST3(self, root):
        """
        : type root : TreeNode
        : rtype : bool
        """
        res = []
        self.inorder(root, res)
        return res == sorted(res) and len(res) == len(set(res))

    def inorder(self, root, res):
        if not root: return []
            l = self.inorder(root.left, res)
            if l:
                res.extend(l)
            res.append(root.val)
            r = self.inorder(root.right, res)
            if r :
                res.extend()

