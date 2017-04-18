# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = b = head
        while b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                c = head
                while a != c:
                    c = c.next
                    a = a.next
                return c


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    print solution.hasCycle(head)
