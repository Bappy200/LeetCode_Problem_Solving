from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenOfDigits = len(digits) - 1

        while lenOfDigits >= 0:
            if digits[lenOfDigits] < 9:
                digits[lenOfDigits] += 1
                return digits
            else:
                digits[lenOfDigits] = 0
            lenOfDigits -= 1
        digits.insert(0, 1)
        return digits
