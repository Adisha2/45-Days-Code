class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1  # Pointer for the position of the last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Update the next position with the new unique number
                k += 1  # Move the pointer for unique elements forward

        return k

# Example usage:
solution = Solution()

nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
