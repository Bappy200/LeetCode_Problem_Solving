class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        result = 0
        prev_result = 0

        while result <= x:
            prev_result = i
            i += 1
            result = i * i

        return prev_result

