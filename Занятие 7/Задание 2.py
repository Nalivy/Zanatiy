s = 0
count = 0
num = int(input())
while num != 0:
    s += num
    count += 1
    num = int(input())
print(s, count)
n = int(input())
x = 0
while x <= n:
    print(x, end=" ")
    x += 5
print()
