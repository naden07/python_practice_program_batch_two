#printing all numbers from 0 to 100 except ending in 0 or 5
for i in range(100):
    if i % 5 != 0:
        print(i)