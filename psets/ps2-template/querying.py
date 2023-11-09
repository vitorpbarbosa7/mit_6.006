def find_rooms(Bs, start, end):
    print(start)
    print(end)

    rooms = 0

    k = 0
    print(Bs[k][1])
    start_guy = Bs[k][1]
    while end > start_guy:
        print(f'Current scan: ', Bs[k])
        rooms += Bs[k][0]
        k +=1
        start_guy = Bs[k][1]
        print('start_guy: ', start_guy)

    print('rooms: ', rooms)
    return rooms


points = [0,2,3,4,6]

Bs = [(1,0,4), (2,2,3), (1,3,4), (2,4,6)]

i = 0

B = []
for i in range(len(points)-1):

    start = points[i]
    end = points[i+1]

    rooms = find_rooms(Bs, start, end)
    B.append((rooms, start, end))

print(B)

    

