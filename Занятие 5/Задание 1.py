t = (5, 2, 9, 1, 7)

if all(isinstance(x, int) for x in t):
    t_sorted = tuple(sorted(t))
    print(t_sorted)
else:
    print(t)
