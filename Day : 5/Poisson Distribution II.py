aX, aY = [float(num) for num in input().split(" ")]

CostX = 160 + 40*(aX + aX**2)
CostY = 128 + 40*(aY + aY**2)

print(round(CostX, 3))
print(round(CostY, 3))
