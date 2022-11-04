# class Solution:
#     def isValid(self, s: str) -> bool:
#         p1 = []
#         p2 = []
#         p3 = []
#
#         for ch in s:
#             if ch == "(":
#                 p1.append(ch)
#             elif ch == ")":
#                 if not p1:
#                     return False
#                 p1.pop()
#             elif ch == "[":
#                 p2.append("[")
#             elif ch == "]":
#                 if not p2:
#                     return False
#                 p2.pop()
#             elif ch == "{":
#                 p3.append("{")
#
#             else:
#                 if not p3:
#                     return False
#                 p3.pop()
#
#         print(p1, p2, p3)
#         return not p1 and not p2 and not p3


class Solution:
    def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        print(opcl)
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                print(stack)
                stack.append(idx)
                print("s", stack)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            else:
                if len(stack) == 0:
                    return False
                re1 = stack.pop()
                print("i", stack)
                print("re1", re1)
                re = opcl[re1]
                if idx != re:
                    return False
            # elif len(stack) == 0 or idx != opcl[stack.pop()]:
            #     return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0

ob = Solution()
result = ob.isValid("([{}])")
print(result)


