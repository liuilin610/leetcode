# 102 Binary Tree Level Order Trversal
# 

# I- DFT
class solution():
    def BinaryTreeLevel(self, root):
        """
        : type root: TreeNode
        : rtype: LIst[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root == None:
            return res
        if len(res) < depth +1:
        res.append([])
        res[depth].append(root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)

# II-BFS
class solution1():
    def BinaryTreeLevel1(self, root):
        """
        : type root: TreeNode
        : rtype: LIst[List[int]]
        """
        res = []
        if root == None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.val for node in q])
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
                q = newq
            return res