class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # Find middle node using slow and fast pointers
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Break the list into two halves
        if prev:
            prev.next = None
        else:
            head = None

        # Middle node becomes root
        root = TreeNode(slow.val)

        # Left half
        root.left = self.sortedListToBST(head)

        # Right half
        root.right = self.sortedListToBST(slow.next)

        return root