# def fibonacci_sum(n):
#     s=0
#     if n<=1:
#         s=n
#         return s
#     else:
#         list=[0,1]
#         for i in range(2,n):
#             list.append(list[i-1]+list[i-2])
#         s=sum(list)
#     return s%10

# def fibonacci_sum(n):
#     sum=1
#     a,b=0,1
#     if n<=1:
#         return n
#     else:
#         for _ in range(n-1):
#             a,b=b,a+b
#             sum+=b
#     return sum%10

# def pisano_period(m): 
#         a, b = 0, 1
#         for i in range(0, m * m): 
#             a, b = b, (a+b)%m 
#             # A Pisano Period starts with 0 and 1 
#             if (a == 0 and b == 1): 
#                 return i + 1

# https://www.youtube.com/watch?v=Nu-lW-Ifyec
            
def fibonacci_sum(n):
    a,b,sum = 0,1,1
    pisano = 60 # Pisano period of modulo 10 
    if n <= 1:
        return n
    else:
        for _ in range((n-1)%pisano):
            a, b = b, (a + b)%10
            sum+=b
        return sum%10
        
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))