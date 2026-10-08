k,n,w = map(int,input().split())
summing = w * k * (w + 1) // 2
borrowing = summing - n
print(borrowing if borrowing > 0 else 0)