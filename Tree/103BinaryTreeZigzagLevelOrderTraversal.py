# 103 Binary Tree Zigzag Level Order Traversal

# I
class solution():
    def ZigzagLevelOrder(self, root):
        """
        : type root :
        : rtype : List[List[int]]
        """
        if not root : return []
        q = collections.deque([root])
        res = []
        level = 0 
        while q:
            tmp_level =[]
            size = len(q)
            for i in range(size):
                tmp = q.popleft()
                if tmp.left : q.append(tmp.left)
                if tmp.right : q.append(tmp.right)
                tmp_level.append(tmp.val)
            res.append(tmp_level[::-1] if level & 1 else tmp_level)
            level += 1
        return res

# II 
class solution1():
    def ZigzagLevelOrder1(self, root):
        """
        : type root :
        : rtype : List[List[int]]
        """
        if not root : return []
        q = collections.deque([root])
        res = []
        level = 0
        while q:
            size = len(q)
            tmp_level = [0]*size:
            for i in range(size):
                tmp = q.popleft()
                if tmp.left : q.append(tmp.left)
                if tmp.right : q.append(tmp.right)
                index = (size - i -1) if level & 1 else i
                tmp_level[index] = tmp.val
            res.append(tmp_level)
            level += 1
        return res
        