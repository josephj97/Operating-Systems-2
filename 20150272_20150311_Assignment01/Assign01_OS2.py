
def bankersAlg(avail, alloc, need):
    cnt = 0
    i = 0
    while i < len(need):
        if  avail[0] >= need[i][0] >= 0 and avail[1] >= need[i][1] >= 0 and avail[1] >= need[i][1] >= 0:
            #print(avail[0], avail[1], avail[2])
            avail[0] = avail[0]+alloc[i][0]
            avail[1] = avail[1]+alloc[i][1]
            avail[2] = avail[2]+alloc[i][2]
            for j in range(0, 3):
                need[i][j] = -1
            print("P", i)
            cnt += 1
            if cnt == len(need):
                break
        if i==len(need)-1:
            i = 0
        else:
            i += 1


allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]
available = [3, 3, 2]
need = [
    [7, 4, 3],
    [1, 2, 2],
    [6, 0, 0],
    [0, 1, 1],
    [4, 3, 1],
]
bankersAlg(available, allocation, need)