t = (1, 3, 5, 2, 3, 7, 3)
elem = 3

if elem in t:
    first = t.index(elem)
    try:
        second = t.index(elem, first + 1)
        print(t[first:second + 1])
    except ValueError:
        print(t[first:])
else:
    print(())
