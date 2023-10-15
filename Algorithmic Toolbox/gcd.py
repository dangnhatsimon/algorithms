# def gcd(a,b):
#     best=0
#     for d in range(1,min(a,b)+1):
#         if (a%d==0) and (b%d==0):
#             best = d
#     return best
    
# def gcd(a,b):
#     if b==0:
#         return a
#     a_remainder=a%b
#     return gcd(b,a_remainder)

# def gcd(a,b):
#     for i in range(min(a,b),0,-1):
#         if (a%i==0) and (b%i==0):
#             return i
#             break

# def gcd(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def gcd(a, b):
    if a==0:
        return b
    if b==0:
        return a
    while b!=0:
        a,b=b,a%b
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
