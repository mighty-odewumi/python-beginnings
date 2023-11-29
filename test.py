
friends = ["Jim", "Karen", "Mike"]

for numbers in range(6):
    if numbers == 0:
        print("First iteration")
    else:
        print("Second iteration")

def raise_to_power(base_num, power_num):
    result = 1
    for ans in range (power_num):
        result = result * base_num
    return result


print(raise_to_power(2,4))


number_grid = [
    [0],
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(row)
