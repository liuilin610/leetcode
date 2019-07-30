# Leetcode 104 Maximum Depth of Binary Tree
#BFS

class Solution:
    def maxDepth(self, root):
    """
    type root : Tree Node
    rtype : int
    """
    que = collections.deque()
    que.qppend(root)
    while que:
        size = len(que)
        for _ in range(size):
            node = que.popleft()
            if not node:
                continue
            que.qppend(node.left)
            que.qppend(node.right)
        depth +=1
    return depth-1

#DFS

class Solution:
    def maxDepth2(self, root):
        """
        :type root: Tree node
        :rtype :int
        """
        if not root:
            return 0
        return 1+ max(self.maxDepth2(root.left), self.maxDepth2(root.right))