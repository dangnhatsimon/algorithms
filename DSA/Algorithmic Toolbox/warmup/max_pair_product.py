def max_pair_product(ls):
    max_pair=0
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]*ls[j]>=max_pair:
                max_pair=ls[i]*ls[j]
    return max_pair

if __name__ == '__main__':
    n = input()
    input_numbers = list(map(int, n.split()))
    print(max_pair_product(input_numbers))


# def max_pair_product(ls):
#     ls.sort(reverse=True)
#     return ls[0]*ls[1]

# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = list(map(int, input().split()))
#     print(max_pair_product(input_numbers))
