# 87711540
"""Broken array search."""


def broken_search(nums, target):
    """Binary search modification."""
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    """Test."""
    nums = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(nums, 5) == 6
