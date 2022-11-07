from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy_nums = nums[::]

        for i in copy_nums:
            if i == val:
                nums.remove(i)
        return len(nums)
