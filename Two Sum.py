from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i, j)
                    result.extend([i, j])
                    break

        return result


ob = Solution()
result = ob.twoSum([3,2,4], 6)
print(result)