from collections.abc import Hashable

data = [1, 2, (3, 4), [5, 6], "hello", {1: 2}]

result = set()
for item in data:
    if isinstance(item, Hashable):
        result.add(item)

print("Множество:", result)
