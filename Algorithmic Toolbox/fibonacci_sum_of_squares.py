# def fibonacci_sum_square(n):
#     s=0
#     if n<=1:
#         s=n
#         return s
#     else:
#         list=[0,1]
#         for i in range(2,n+1):
#             list.append(list[i-1]+list[i-2])
#         s=sum(map(lambda i: i**2,list))
#         return s

# def fibonacci_sum_square(m,n):
#     a,b=0,1
#     if (n<=1) and (m<=n):
#         return n
#     if n>1:
#         for _ in range(m):
#             a,b=b,a+b
#         partial_sum=a+b
#         if (m<n):
#             for _ in range (m,n-1):
#                 a,b=b,a+b
#                 partial_sum+=b
#             return partial_sum%10
#         if  m==n:
#             return a%10
        
# def fibonacci_sum_square(n):
#     a,b=0,1
#     squared_sum=0
#     if (n<=1):
#         return n
#     else:
#         for _ in range (n):
#             squared_sum+=b**2
#             a,b=b,a+b
#         return squared_sum%10

# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_sum_square(n))

# def pisano_period(m): 
#         a, b = 0, 1
#         for i in range(0, m * m): 
#             a, b = b, (a+b)%m 
#             # A Pisano Period starts with 0 and 1 
#             if (a == 0 and b == 1): 
#                 return i + 1

# https://www.youtube.com/watch?v=Nu-lW-Ifyec

# def fibonacci_sum_square(n):
#     a,b,squares_sum = 0,1,1
#     pisano = 60 # Pisano period of modulo 10 
#     if n <= 1:
#         return n
#     else:
#         for _ in range((n-1)%pisano):
#             a, b = b, (a + b)
#             squares_sum+=b**2
#         return squares_sum%10

# For n≥1 the inductive step then would be: From the inductive hypothesis we have
# https://math.stackexchange.com/questions/2613609/summation-of-squares-of-fibonacci-numbers


def fibonacci(n):
    a,b=0,1
    pisano = 60 # Pisano period of modulo 10 
    if n <= 1:
        return n
    else:
        for _ in range((n-1)%pisano):
            a, b = b, (a + b)
        return b
def fibonacci_sum_square(n):
    return fibonacci(n)*fibonacci(n+1)%10        
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_square(n))