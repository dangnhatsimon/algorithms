class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.upper()
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        result = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if (s[i] == 'I' and s[i+1] in ['V','X']) or (s[i] == 'X' and s[i+1] in ['L','C']) or (s[i] == 'C' and s[i+1] in ['D','M']):
                    result += dict[s[i+1]] - dict[s[i]]
                    i += 2
                else:
                    result += dict[s[i]]
                    i += 1
            else:
                    result += dict[s[i]]
                    i += 1
        return result
