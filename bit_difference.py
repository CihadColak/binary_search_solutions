def solve(x, y):
    xBin = str(bin(x))[2:]
    yBin = str(bin(y))[2:]
    if len(xBin) < len(yBin):
        xBin = "0" + xBin
    elif len(xBin) > len(yBin):
        yBin = "0" + yBin
    count = 0
    for xVal, yVal in zip(xBin, yBin):
        if xVal != yVal:
            count += 1
    return count


print(solve(1347477588, 339414349))
