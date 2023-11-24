n = int(input())

elements = set()

for _ in range(n):
    new_element = input().split()
    for el in new_element:
        elements.add(el)

print(*elements, sep='\n')
