from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy_num = nums[0]
        k = 1

        for i in range(1, len(nums)):
            if nums[i] > copy_num:
                k += 1
                copy_num = nums[i]

        return k

ob = Solution()
result = ob.removeDuplicates([1, 1, 2])
print(result)