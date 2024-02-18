# def fibonacci_modulo(n,m):
#     if n<=1:
#         return n%m
#     else:
#         list=[0,1]
#         for i in range(2,n+1):
#             list.append(list[i-1]+list[i-2])
#     return list[n]%m

# def fibonacci_modulo(n,m):
#     if n<=1:
#         return n
#     else:
#         a,b=0,1
#         for _ in range(n-1):
#             a,b=b,a+b
#     return b%m

# https://www.youtube.com/watch?v=Nu-lW-Ifyec

def pisano_period(m): 
        a, b = 0, 1
        for i in range(0, m * m): 
            a, b = b, (a+b)%m 
            # A Pisano Period starts with 0 and 1 
            if (a == 0 and b == 1): 
                return i + 1
            
def fibonacci_modulo(n,m):
    a,b=0,1
    if n <= 1:
        return n
    else:
        for _ in range((n - 1)%pisano_period(m)):
            a, b = b, (a + b)%m
        return b
       
if __name__ == '__main__':
    n,m=map(int,input().split())
    print(fibonacci_modulo(n,m))
    