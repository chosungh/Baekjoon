x, y, w, h = map(int, input().split())
a = abs(w-x)
b = abs(x-0)
c = abs(h-y)
d = abs(y-0)



print(min(a, b, c, d))