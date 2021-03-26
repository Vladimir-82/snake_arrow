n = 3
arrow = [[0]*n for i in range(n)]

index_first = 0
index_second = 0

round = 0
start = 1
finish = n
counter = 0
for k in range(len(arrow)):
    while 0 in arrow[k]:

        if round != 0:
            start = finish
            finish = start + (n - 1 - round)

        for i in range(start, finish):
            arrow[index_first][index_second] = i
            counter += 1
            index_second += 1
            if index_second == n - round:
                break
        if counter >= n * n:
            break


        start = finish
        finish = start + (n - 1 - round)

        for i in range(start, finish):

            arrow[index_first][index_second] = i
            counter += 1

            index_first += 1
            if index_first == n - round:
                break
        if counter >= n * n:
            break


        start = finish
        finish = start + (n - 1 - round)

        for i in range(start, finish):

            arrow[index_first][index_second] = i
            counter += 1
            index_second -= 1
            if index_second == round:
                break
        if counter >= n * n:
            break

        start = finish
        finish = start + (n - 2 - round)
        for i in range(start, finish):
            arrow[index_first][index_second] = i
            counter += 1
            index_first -= 1
            if index_first == round:
                break
        if counter >= n * n:
            break

    round += 1

print(arrow)



# n = 3
# arrow = [[0]*n for i in range(n)]
# index_first = 0
# index_second = 0
# round = 0
# for i in range(1, n * n + 1):
#     arrow[index_first][index_second] = i
#     index_second += 1
#
#     if index_second == n:
#         break
# print(arrow)