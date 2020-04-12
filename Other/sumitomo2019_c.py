x = int(input())
mod = x%100

minbuy = 0
for i in range(1,6)[::-1]:
    minbuy += mod // i
    mod = mod % i
print(0 if minbuy*100 > x else 1)