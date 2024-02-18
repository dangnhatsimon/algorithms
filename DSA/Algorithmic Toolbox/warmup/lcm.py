def LCM(a,b):
    for i in range(min(a,b),a*b+1,min(a,b)):
        if i%max(a,b)==0:
            return i
            break

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(LCM(a, b))