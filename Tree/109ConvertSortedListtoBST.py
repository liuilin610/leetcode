# 109 Convert Sorted List to BST

# I fast/slow
# O(NlogN)
class solution():
    def SortedListtoBST(self, head):
        """
        : type head : ListNode
        : rtype : TreeNode
        """
        def Construct(head, tail):
            if head == tail : return None
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow, fast = slow.next, fast.next.next
            root = TreeNode(slow.val)
            root.left = Construct(head, slow)
            root.right = Construct(slow.next, tail)
            return root
        return SortedListtoBST(head, None)

# II
class solution1():
    def SortedListtoBST1(self, head):
        """
        : type head : ListNode
        : rtype : TreeNode
        """
        return None if not head else self.Construct1(head, None)

     def Construct1(head, tail):
         if head == tail: return None
        slow = fast = head
        while fast != tail and fast.next != tail :
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.Construct1(head, slow)
        root.right = self.Construct1(slow +1, tail)
        return root

# III List-> array
class solution2():
    def SortedListtoBST2(self, head):
        """
        : type head : ListNode
        : rtype : TreeNode
        """ 
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.helper(nums)
    def helper(self, nums):
        if not nums: return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums[: mid])
        root.right = self.helper(nums[mid+1:])
        return root
        
class solution3():
    def SortedListtoBST3(self, head):
        """
        : type head : ListNode
        : rtype : TreeNode
        """
        if not head: return None
            tail, length = head, 0
        while tail:
            tail, length = tail.next, length+1
            return self.dfs(head, 0, length-1)

        def dfs(self, head, L, R):
            if L == R : return TreeNode(head.val)
            if L > R: return None
            mid, ct, tmp = (L+R)>>1, L, head
            while ct < mid : ct, tmp = ct+1, tmp.next
                root = TreeNode(tmp.val)
                root.left, root.right = self.dfs(head, L,mid-1), self.dfs(tmp.next, mid+1, R)
                return root
            