a = [input() for _ in range(9)]
a = list(map(int, a))
max_value = int(max(a))

print(max(a))
print(a.index(max_value)+1)