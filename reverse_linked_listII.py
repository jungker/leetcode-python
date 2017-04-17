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
        for i in range(n - 1):
            q = q.next
        t1 = p.next if p else None
        t2 = q.next if q else None
        tt = t2.next
        p.next = t2
        if t1.next == t2:
            t2.next = t1
        else:
            t2.next = t1.next
            q.next = t1
        t1.next = tt
        return res.next


if __name__ == '__main__':
    p = ListNode(1)
    p.next = ListNode(2)
    p.next.next = ListNode(3)
    p.next.next.next = ListNode(4)
    p.next.next.next.next = ListNode(5)

    solution = Solution()
    m, n = 2, 4
    res = solution.reverseBetween(p, 1, 5)
    printListNode(res)
