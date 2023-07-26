def countingValleys(steps, path):
    count = 0
    sea_level = 0
    for i in range(steps):
        if path[i] == "D":
            sea_level -= 1
        else:
            sea_level += 1
            if sea_level == 0:
                count += 1
    
    return count

print(countingValleys(8, "UDDDUDUU"))