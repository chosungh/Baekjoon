num_list = list(map(int, input().split()))

ty = None
ascending = True
descending = True

for i in range(1, len(num_list)):
    if num_list[i] != num_list[i-1]+1:
        ascending = False
    if num_list[i] != num_list[i-1]-1:
        descending = False

if ascending:
    ty = 'ascending'
elif descending:
    ty = 'descending'
else:
    ty = 'mixed'

print(ty)