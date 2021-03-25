n = 2
arrow = [[] for i in range(n)]
counter = 0
for i in range(1, n * n + 1):
    arrow[counter].append(i)
    if len(arrow[counter]) == n:
        counter += 1
print(arrow)