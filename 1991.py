def f(root, tree):
    if root == '.':
        return
    print(root, end='')

    f(tree[root][0], tree)
    f(tree[root][1], tree)

def m(root, tree):
    if root == '.':
        return
    m(tree[root][0], tree)
    print(root, end='')
    m(tree[root][1], tree)

def l(root, tree):
    if root == '.':
        return
    l(tree[root][0], tree)
    l(tree[root][1], tree)
    print(root, end='')

num = int(input())
tree = {}

for i in range(num):
    root, left, right = input().split()
    tree[root] = [left, right]

f('A', tree)
print()
m('A', tree)
print()
l('A', tree)