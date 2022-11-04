class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total_int = 0
        temp = symbol_value.get(s[0])

        for i in s:
            current_value = symbol_value.get(i)

            if temp >= current_value:
                total_int += current_value
                temp = current_value
            else:
                total_int += current_value - temp * 2
                temp = current_value

        return total_int

