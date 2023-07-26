def hourglassSum(arr):
    highest = -10000
    for i in range(1, 5):
        for j in range(1, 5):
            hrgls_sum = 0
            hrgls_sum = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i-1][j-1] + arr[i+1][j-1] + arr[i-1][j+1]
            if hrgls_sum > highest:
                highest = hrgls_sum
            
    return highest 




arr = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]

print(hourglassSum(arr))