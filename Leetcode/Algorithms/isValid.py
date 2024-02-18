class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s)%2 != 0:
            return False
        for char in s:
            if char in map_dict:
                stack.append(char)
            elif len(stack) != 0 and char == map_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0