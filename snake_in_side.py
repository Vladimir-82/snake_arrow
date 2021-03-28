def to_right(arrow, index_first, index_second, elem):
    while True:
        arrow[index_first][index_second] = elem
        index_second += 1
        elem += 1
        if index_second == n or arrow[index_first][index_second] != 0:
            return arrow, index_first + 1, index_second - 1, elem

def to_down(arrow, index_first, index_second, elem):
    while True:
        arrow[index_first][index_second] = elem
        index_first += 1
        elem += 1
        if index_first == n or arrow[index_first][index_second] != 0:
            return arrow, index_first - 1, index_second - 1, elem

def to_left(arrow, index_first, index_second, elem):
    while True:
        arrow[index_first][index_second] = elem
        index_second -= 1
        elem += 1

        if arrow[index_first][index_second] != 0:
            return arrow, index_first - 1, index_second + 1, elem
        if index_second == 0:
            return arrow, index_first, index_second, elem

def to_up(arrow, index_first, index_second, elem):
    while True:
        arrow[index_first][index_second] = elem
        index_first -= 1
        elem += 1
        if arrow[index_first][index_second] != 0:
            return arrow, index_first + 1, index_second + 1, elem

n = 7
arrow = [[0]*n for _ in range(n)]
index_first = 0
index_second = 0
elem = 1
while True:
    arrow, index_first, index_second, elem = to_right(arrow, index_first, index_second, elem)
    if elem >= n * n + 1:
        break
    arrow, index_first, index_second, elem = to_down(arrow, index_first, index_second, elem)
    if elem >= n * n + 1:
        break
    arrow, index_first, index_second, elem = to_left(arrow, index_first, index_second, elem)
    if elem >= n * n + 1:
        break
    arrow, index_first, index_second, elem = to_up(arrow, index_first, index_second, elem)
    if elem >= n * n + 1:
        break

for _ in arrow:
    print(_)