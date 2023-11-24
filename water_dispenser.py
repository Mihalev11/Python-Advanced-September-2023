from collections import deque

quantity = int(input())
water_line = deque()
liters_to_add = 0

name = input()

while name != "Start":
    water_line.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        if liters_to_give <= quantity:
            person_name = water_line.popleft()
            print(f"{person_name} got water")
            quantity -= liters_to_give
        else:
            print(f"{person_name} must wait")
    else:
        liters_to_add = int(data[1])
        quantity += liters_to_add

    command = input()

print(f"{quantity} liters left")
