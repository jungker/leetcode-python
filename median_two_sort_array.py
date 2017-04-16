class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        if not size:
            return 0
        if size % 2:
            return self.findKthNumber(nums1, nums2, size / 2 + 1)
        else:
            return (self.findKthNumber(nums1, nums2, size / 2)
                    + self.findKthNumber(nums1, nums2, size / 2 + 1)) / 2.0

    def findKthNumber(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findKthNumber(nums2, nums1, k)
        if not m:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        ia = min(k / 2, m)
        ib = k - ia
        if nums1[ia - 1] < nums2[ib - 1]:
            return self.findKthNumber(nums1[ia:], nums2, k - ia)
        elif nums1[ia - 1] > nums2[ib - 1]:
            return self.findKthNumber(nums1, nums2[ib:], k - ib)
        else:
            return nums1[ia - 1]


if __name__ == '__main__':
    x = [1, 3, 5]
    y = [2, 4, 6, 7]
    solution = Solution()
    print solution.findMedianSortedArrays(x, y)
