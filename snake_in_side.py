n = 3
arrow = [[0]*3 for i in range(n)]
counter_first = 0
counter_second = 0
for i in range(1, n * n + 1):
    arrow[counter_first][counter_second] = i
    counter_second += 1
    if counter_second == n:
        break


print(arrow)