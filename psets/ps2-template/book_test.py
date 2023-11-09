B1 = (2,2,3)
B2 = (1,0,4)

Bs = [B1,B2]

start_i = B1[i][1]
start_j = B2[j][1]

j = cont
i = cont + 1

rooms_i = Bs[i][0]
rooms_j = Bs[j][0]
while i + j < 2*len(Bs): 

	# Inicializacao

	# use start from some, walk in the same 

	if start_j < start_i:
		if start > start_j:
			# keep same start
			pass
		else:
			start = start_j
			rooms += rooms_j
	
		if end_i < end_j:
			start = end_i
		else:
			start = end_j
			
		end = start_i
		rooms += rooms_j

	else:
		start = start_i
		end = start_j
		rooms += rooms_i

	new_element = (rooms, marker, end)
	
	start = end

	
