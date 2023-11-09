B1 = [(2,2,3),(1,3,4)]
B2 = [(1,0,4),(2,4,6)]

cont = 0

i = 0
j = 0

B = []

finished_i = False
finished_j = False

rooms_j = B2[j][0]
rooms_i = B1[i][0]


start_j = B2[j][1]
start_i = B1[i][1]


end_j = B1[j][2]
end_i = B1[i][2]

marker_j = start_j
marker_i = start_i

rooms = 0

while i < len(B1) and j < len(B2): 

    if marker_j < marker_i:
        rooms += rooms_j 
        start = start_j
        end = start_i
    else:
        rooms += rooms_i
        start = start_i
        end = start_j

        start = start_i
        end = start_j

    
    if finished_i:
        i += 1
    
    if finished_j:
        j += 1