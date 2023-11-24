clothes_Stack = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while clothes_Stack:
    racks += 1
    current_rack_capacity = rack_capacity
    while clothes_Stack and clothes_Stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_Stack.pop()

print(racks)



