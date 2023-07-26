def countingValleys(steps, path):
    count = 0
    sea_level = 0
    i = 0
    while i <= steps-1:
        sea_level += 1 if path[i] == "U" else -1
        if sea_level == 0 and path[i] == "U":
            count += 1
        i += 1
            
    return count
    

print(countingValleys(8, "UDDDUDUU"))