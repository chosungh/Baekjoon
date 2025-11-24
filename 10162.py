num = int(input())
timers = [300, 60, 10]
res = []

for timer in timers:
    res.append(num // timer)
    num %= timer

if num == 0:
    print(*res)
else: print(-1)