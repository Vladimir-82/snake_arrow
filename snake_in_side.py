def up():
    pass
def right():
    pass
def down():
    pass
def left():
    pass


n = 3
arrow = [[0]*n for i in range(n)]
index_first = 0
index_second = 0
round = 0
for i in range(1, n * n + 1):
    up()
    # arrow[index_first][index_second] = i
    # index_second += 1
    #
    # if index_second == n - 1:
    #     index_second = n - 1 - round
    #     index_first += 1



print(arrow)