a, b = map(int, input().split())
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    print(i, end=" ")
print()
for i in range(b, a - 1, -1):
    print(i)
p = int(input())
masses = list(map(int, input().split()))
if sum(masses) <= p:
    print("Перевозка возможна")
else:
    print("Перевозка невозможна")
