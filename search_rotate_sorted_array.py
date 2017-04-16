class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size < 1:
            return -1
        lo = 0
        hi = size - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == '__main__':
    # x = [4, 5, 6, 7, 0, 1, 2]
    # x = [1, 1, 1, 3, 1]
    x = [3, 1]
    solution = Solution()
    print solution.search(x, 1)
