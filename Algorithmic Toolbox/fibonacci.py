# def FibRecurs(n):
#     if n<=1:
#         return n
#     else:
#         return FibRecurs(n-1)+FibRecurs(n-2)
    
# def FibList(n):
#     if n<=1:
#         return n
#     else:
#         list=[0,1]
#         for i in range(2,n+1):
#             list.append(list[i-1]+list[i-2])
#     return list[n]

# https://www.youtube.com/watch?v=Nu-lW-Ifyec

def fibonacci(n):
    if n<=1:
        return n
    else:
        a,b=0,1
        for _ in range(n):
            a,b=b,a+b
    return a

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))