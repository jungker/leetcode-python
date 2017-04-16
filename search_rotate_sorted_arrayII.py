class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        size = len(nums)
        if size < 1:
            return False
        lo = 0
        hi = size - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1
        return False


if __name__ == '__main__':
    x = [1, 3, 1, 1, 1]
    solution = Solution()
    print solution.search(x, 3)
