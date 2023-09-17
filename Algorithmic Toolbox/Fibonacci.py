# def FibRecurs(n):
#     if n<=1:
#         return n
#     else:
#         return FibRecurs(n-1)+FibRecurs(n-2)
    
def FibList(n):
    if n<=1:
        return n
    else:
        list=[0,1]
        for i in range(2,n+1):
            list.append(list[i-1]+list[i-2])
    return list[n]

if __name__ == '__main__':
    n = int(input())
    print(FibList(n))