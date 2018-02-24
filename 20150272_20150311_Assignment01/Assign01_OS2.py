def compare_arrays(arr1, arr2):
    for i in range(len(arr1)):
        if not(arr1[i] >= arr2[i] >= 0):
            return False
    return True


def add_arrays(avail, alloc):
    return [avail[i] + alloc[i] for i in range(len(alloc))]


def bankersAlg(avail, alloc, maximum):
    cnt = 0
    i = 0
    lastvisit = 0
    need = [[maximum[i][j] - alloc[i][j] for j in range(len(maximum[i]))]for i in range(len(maximum))]
    status = ""
    if compare_arrays(avail, need[0]):
        avail = add_arrays(avail, alloc[0])
        need[0] = [-1, -1, -1]
        status += "P{}".format(i)
        cnt += 1

    i = 1
    while True:
        if compare_arrays(avail, need[i]):
            avail = add_arrays(avail, alloc[i])
            need[i] = [-1, -1, -1]
            status += "P{}".format(i)
            cnt += 1
            if cnt == len(need):
                break

        elif lastvisit == i:
            status = "Unsafe state"
            break

        if i == len(need)-1:
            i = 0

        else:
            i += 1

    return status


def take_2d_array(length, width, Str):
    print("Please Enter", Str, "{} * {} grid".format(length, width))
    arr = list(list(map(int, input().split()))for i in range(length))
    return arr


def take_1d_array(length ,Str):
    print("Please Enter", Str , "array of length {} ".format(length))
    # arr = [int(input()) for i in range(length)]
    arr = list(map(int, input().split()))
    return arr

def calc_available(avail, alloc):
    for i in range(len(alloc)):
        for j in range(len(avail)):
            avail[j] -= alloc[i][j]
    return avail

def request_resources(avail, alloc, maximum, pnum, request):
    status = bankersAlg(avail, alloc, maximum)
    if status == "Unsafe state":
        print("Unsafe state")
        return avail, alloc, maximum

    need = [[maximum[i][j] - alloc[i][j] for j in range(len(maximum[i]))]for i in range(len(maximum))]

    if compare_arrays(need[pnum], request) and compare_arrays(avail, request):
        avail = [avail[i] - request[i] for i in range(len(request))]
        need[pnum] = [need[pnum][i] - request[i] for i in range(len(request))]
        alloc[pnum] = add_arrays(alloc[pnum], request)
        status = bankersAlg(avail, alloc, maximum)
        if status == "Unsafe state":
            print("Unsafe request1")
            avail = add_arrays(avail, request)       #[avail[i] + request[i] for i in range(len(request))]
            need[pnum] = add_arrays(need[pnum], request)  # [need[pnum][i] + request[i] for i in range(len(request))]
            alloc[pnum] = [alloc[pnum][i] - request[i] for i in range(len(request))]

            return avail, alloc, maximum
        else:
             print("Safe request")
             return avail, alloc, maximum
    else:
        print("Unsafe request")
        return avail, alloc, maximum




def main():
    process = int(input("Enter number of process: "))
    resources = int(input("Enter number of resources: "))

    # allocation = [
    #     [0, 1, 0],
    #     [2, 0, 0],
    #     [3, 0, 2],
    #     [2, 1, 1],
    #     [0, 0, 2],
    # ]
    # maximum = [
    #     [7, 5, 3],
    #     [3, 2, 2],
    #     [9, 0, 2],
    #     [2, 2, 2],
    #     [4, 3, 3],
    # ]
    # available = [3, 3, 2]

    available = take_1d_array(resources,'Available')
    print("Available: ", available)
    maximum = take_2d_array(process, resources, 'Maximum')
    print("Maximum: ", maximum)
    allocation = take_2d_array(process, resources, 'Allocation')
    print("allocation:", allocation)
    available = calc_available(available, allocation)
    print("New Available is: ", available)

    print(bankersAlg(available, allocation, maximum))

    while True:
        query = input().split()
        if len(query) == 0:
            continue
        if query[0].lower() == "quit":
            break
        query = list(map(int, query[1:]))
        available, allocation, maximum = request_resources(available, allocation, maximum, int(query[0]), query[1:])
        print("Available : ", available)
        print("maximum   : ", maximum)
        print("allocated :", allocation)


if __name__ == "__main__":
    main()

'''
3 3 2
10 5 7
7 5 3
3 2 2
9 0 2 
2 2 2
4 3 3
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
'''