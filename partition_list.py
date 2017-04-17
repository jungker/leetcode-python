# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(p):
    while p:
        print p.val,
        p = p.next
    print


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p0 = p = ListNode(0)
        q0 = q = ListNode(0)
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            elif head.val >= x:
                q.next = head
                q = q.next
            head = head.next
        p.next = q0.next
        q.next = None
        return p0.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    solution = Solution()
    res = solution.partition(head, 3)
    printListNode(res)
