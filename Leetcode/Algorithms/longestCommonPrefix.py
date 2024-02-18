class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = ''
        checked = False
        for i, char in enumerate(min(strs, key = len)):
            if all(char == string[i] for string in strs):
                result += char
            else:
                break
        return result