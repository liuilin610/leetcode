# 111 Minimum Depth of Binary Tree

# I- DFS
class solution():
    def minDepth(self, root):
        """
        : type root : TreeNode
        : rtype : int
        """
        if not root: return 0
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if not left:
                return right+1
            if not right:
                return left+1
                return 1+min(left,right)

# II-BFS
class solution1():
    def minDepth1(self, root):
        """
        : type root : TreeNode
        : rtype : int
        """
        if root == None: return 0
        depth = 0
        q = [root]
        while len(q) !=0:
            depth += 1
            for i in range(0, len(q)):
                if not q[0].left and not q[0].right
                    return depth
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        return depth