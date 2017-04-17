# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(p):
    while p:
        print p.val,
        p = p.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = 0
        res = t = ListNode(0)
        while l1 or l2 or r:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            c = a + b + r
            t.next = ListNode(c % 10)
            t = t.next
            r = c / 10
        return res.next


if __name__ == '__main__':
    p = ListNode(2)
    p.next = ListNode(4)
    p.next.next = ListNode(3)

    q = ListNode(5)
    q.next = ListNode(6)
    q.next.next = ListNode(4)

    solution = Solution()
    res = solution.addTwoNumbers(p, q)
    printListNode(res)
