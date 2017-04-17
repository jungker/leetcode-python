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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = p = q = ListNode(0)
        res.next = head
        for i in range(m - 1):
            p = p.next
        p0 = p
        p = p.next
        for i in range(n):
            q = q.next
        while p != q:
            t = p
            p = p.next
            t.next = q.next
            q.next = t
        p0.next = q
        return res.next


if __name__ == '__main__':
    p = ListNode(1)
    p.next = ListNode(2)
    p.next.next = ListNode(3)
    p.next.next.next = ListNode(4)
    p.next.next.next.next = ListNode(5)

    solution = Solution()
    m, n = 2, 4
    res = solution.reverseBetween(p, 4, 5)
    printListNode(res)
