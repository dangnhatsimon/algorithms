def change(money: int) -> int:
    if money == 0:
        return 0
    coin = [10,5,1]
    no_coin = 0
    for i in range(len(coin)):
        no_coin += money // coin[i]
        money = money % coin[i]
    return no_coin
        
if __name__ == '__main__':
    m = int(input())
    print(change(m))