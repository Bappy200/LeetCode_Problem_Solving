class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split().pop()
        return len(last_word)