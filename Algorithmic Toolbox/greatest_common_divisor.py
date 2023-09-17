# def NaiveGCD(a,b):
#     best=0
#     for d in range(1,min(a,b)+1):
#         if (a%d==0) and (b%d==0):
#             best = d
#     return best
    
def EuclidGCD(a,b):
    if b==0:
        return a
    a_remainder=a%b
    return EuclidGCD(b,a_remainder)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(EuclidGCD(a, b))