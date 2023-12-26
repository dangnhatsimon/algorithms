def LookandSaySequence(num):
    num = str(num)
    while i < len(num):
        count = 1
        while i+1 < len(num) and num[i] == num[i+1]:
            i += 1
            count += 1
        result.append(str(count) + num[i])
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    num =input()
    result = LookandSaySequence(num)
    print(result)