inp = [float(i) for i in input().split()]
n = inp[0]
a = inp[1]
b = inp[2]
for i in range(1000):
    n = a * n - b * n * n
    if n <= 0:
        break
    print(n)
print(n)