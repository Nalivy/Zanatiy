import math

a = []
b = []

a.append(4.5)
a.append(3.4)
a.extend([8.7, 1.3])

b.append(14.5)
b.append(3.4)
b.extend([8.7, 11.3])

a.insert(1, 100)
a.insert(3, 100)

b.insert(0, 200)
b.insert(2, 200)

print("Исходные списки:")
print("1-й:", a)
print("2-й:", b)

del a[0]
del b[0]

a.remove(100)
b.remove(200)

print("\nПосле удалений:")
print("1-й:", a)
print("2-й:", b)

sa = set(a)
sb = set(b)
sa_and_sb = sa & sb

print("\nУникальные элементы:")
print("1-й:", sa)
print("2-й:", sb)
print("общие:", sa_and_sb)

c = a + b
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

even_elements = c[::2]
sr_ar = sum(even_elements) / len(even_elements)

odd_elements = c[1::2]
product = 1
for num in odd_elements:
    product *= num
sr_geom = product ** (1 / len(odd_elements))

c_max = max(c)
c_min = min(c)

print("\nИтоговые:")
print("3-й:", c)
print("Сортировка (возр.):", c_asc)
print("Сортировка (убыв.):", c_desc)
print(f"Ср. арифм. = {sr_ar:.2f}, ср. геометр. = {sr_geom:.2f}")
print("Макс. и мин.:", c_max, c_min)
