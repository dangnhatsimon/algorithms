# def partial_fibonacci_sum(m,n):
#     s=0
#     if n<=1:
#         s=n
#         return s
#     else:
#         list=[0,1]
#         for i in range(2,n+1):
#             list.append(list[i-1]+list[i-2])
#         for i in range (m,n+1):
#             s+=list[i]
#         return s

# def partial_fibonacci_sum(m,n):
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
              
# def partial_fibonacci_sum(m,n):
#     a,b=0,1
#     partial_sum=0
#     if (n<=1):
#         return n
#     else:
#         for i in range (n):
#             a,b=b,a+b
#             if (i>=m-1):
#                 partial_sum+=a
#         return partial_sum%10

# def pisano_period(m): 
#         a, b = 0, 1
#         for i in range(0, m * m): 
#             a, b = b, (a+b)%m 
#             # A Pisano Period starts with 0 and 1 
#             if (a == 0 and b == 1): 
#                 return i + 1

# https://www.youtube.com/watch?v=Nu-lW-Ifyec
            
# def partial_fibonacci_sum(m,n):
#     a,b,partial_sum = 0,1,0
#     pisano = 60 # Pisano period of modulo 10 
#     if n <= 1:
#         return n
#     else:
#         for i in range((n+1)%pisano):
#             if i>=(m)%pisano:
#                 partial_sum+=a
#             a, b = b, (a + b)%10
#         return partial_sum%10

# if __name__ == '__main__':
#     m,n=map(int,input().split())
#     print(partial_fibonacci_sum(m,n))

def matrix_multiply(a, b, mod):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod]
    ]

def matrix_power(matrix, n, mod):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result

def fib_modulo_n(n, mod):
    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n - 1, mod)
    return result_matrix[0][0]

def partial_fibonacci_sum(m, n):
    mod = 10
    sum_n = (fib_modulo_n(n + 2, mod) - 1) % mod
    sum_m = (fib_modulo_n(m + 1, mod) - 1) % mod
    return (sum_n - sum_m) % mod

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(partial_fibonacci_sum(m, n))
    