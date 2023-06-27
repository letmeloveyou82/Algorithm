import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input()) # 날의 수
    stock_price = list(map(int, input().split()))
    max_profit = 0
    max = 0
    for i in range(len(stock_price)-1, -1, -1):
        if stock_price[i] > max:
            max = stock_price[i]
        else:
            max_profit += max - stock_price[i]
    print(max_profit)