a, b = input().split()

A = ''.join(reversed(a))
B = ''.join(reversed(b))

if int(A) > int(B):
    print(int(A))
else: print(int(B))