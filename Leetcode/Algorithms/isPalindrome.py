class Solution:
    def isPalindrome(self, x: int) -> bool:
        a,b = x,0
        while a>0:
            b, a = b*10 + a%10, a//10
        return b == x