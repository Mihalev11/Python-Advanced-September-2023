txt = tuple(input())

unique_symbols = sorted(set(txt))

for char in unique_symbols:
    print(f"{char}: {txt.count(char)} time/s")

