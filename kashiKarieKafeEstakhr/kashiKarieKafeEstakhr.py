n, m = input().split()
n = int(n)
m = int(m)
areaOfTiles = 0.2
numberOfTiles = int(n * m / areaOfTiles * 100)
print(numberOfTiles)