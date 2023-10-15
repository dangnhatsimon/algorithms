# def fibonacci_last_digit(n):
#     if n<=1:
#         return n
#     else:
#         list=[0,1]
#         for i in range(2,n):
#             list.append(list[i-1]+list[i-2])
#     return list[-1]%10

# def fibonacci_last_digit(n):
#     if n<=1:
#         return n
#     else:
#         a,b=0,1
#         for _ in range(n-1):
#             a,b=b,a+b
#     return b%10

# def pisano_period(m): 
#         a, b = 0, 1
#         for i in range(0, m * m): 
#             a, b = b, (a+b)%m 
#             # A Pisano Period starts with 0 and 1 
#             if (a == 0 and b == 1): 
#                 return i + 1

# https://www.youtube.com/watch?v=Nu-lW-Ifyec

def fibonacci_last_digit(n):
    pisano = 60 # Pisano period of modulo 10 
    a,b = 0,1
    if n <= 1:
        return n
    else:
        for _ in range((n - 1)%pisano):
            a, b = b, (a + b)%10
        return b
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))