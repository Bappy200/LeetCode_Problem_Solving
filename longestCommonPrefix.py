class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            is_true = True
            for j in range(1, len(strs)):
                try:
                    if strs[0][i] != strs[j][i]:
                        is_true = False
                        break
                except IndexError:
                    return prefix
            if is_true:
                prefix += strs[0][i]
            else:
                return prefix

        return prefix