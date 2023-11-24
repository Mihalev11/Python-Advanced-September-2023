n = int(input())

uni_names = set()

for _ in range(n):
    name = input()
    uni_names.add(name)

for name in uni_names:
    print(name)