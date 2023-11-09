#B1 = [(2,2,3),(1,3,4)]
#B2 = [(1,0,4),(2,4,6)]

cont = 0

j = 0
i = j + 1

Bs = [(1,0,4),(2,2,3),(1,3,4),(2,4,6)]

rooms_i = Bs[i][0]
rooms_j = Bs[j][0]

marker_i = Bs[i][1]
marker_j = Bs[j][1]

rooms = -1

B = []

def _move_tuple(k, marker, rooms = -1):
	print('initial k: ', k)

	initial_marker = marker
	
	if marker == Bs[k][1]:
		# update marker because it is still possible
		marker = Bs[k][2]
	else:
		#moving marker inside tuple is not possible anymore, so move it to next element
		# rooms -= Bs[k][0]
		k +=1
		
		marker = Bs[k][1]

	# if new marker, is equal to initial_marker, go to [2]
	# k já andou
	if marker == initial_marker:
		marker = Bs[k][2]

	print('final k: ', k)

	return k, marker, rooms

# Base case
if marker_j < marker_i:
	start_time = marker_j
	# finalizar um para abrir outro
	end = marker_i
	rooms += rooms_j
	j, marker_j, rooms = _move_tuple(j, marker_j, rooms)
	i, marker_i, rooms = _move_tuple(i, marker_i, rooms)

elif marker_i < marker_j:		

	start_time = marker_i

	end = marker_j
	rooms += rooms_i
	i, marker_i, rooms = _move_tuple(i, marker_i, rooms)
	j, marker_j, rooms = _move_tuple(j, marker_j, rooms)
	
	
new_element = (rooms, start_time, end)
print(new_element)
B.append(new_element)
print(B)

print('marker i ', i, marker_i)
print('marker j ', j, marker_j)

start_time = end


while i < len(Bs): 

	if marker_i <= marker_j:
		end = marker_i
		i, marker_i, rooms = _move_tuple(i, marker_i, rooms)
		rooms = -1

	elif marker_i > marker_j:
		end = marker_j
		j, marker_j, rooms = _move_tuple(j, marker_j, rooms)
		rooms = -1

	new_element = (rooms, start_time, end)
	B.append(new_element)

	start_time = end

	print(B)
	print('marker i ', i, marker_i)
	print('marker j ', j, marker_j)
	print('new start_time: ', start_time)

	
	



