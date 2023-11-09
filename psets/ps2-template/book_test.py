B1 = [(2,2,3)]
B2 = [(1,0,4)]

cont = 0

i = 0
j = 0

B = []
while i < len(B1) and j < len(B2): 

	rooms_i = B1[i][0]
	rooms_j = B2[j][0]
	
	start_i = B1[i][1]
	start_j = B2[j][1]
	
	end_i = B1[i][2]
	end_j = B2[j][2]
	
	if start_j < start_i:
		start_time = start_j
		# finalizar um para abrir outro
		end = start_i
		rooms = rooms_j
	else:
		start_time = start_i
		end = start_j
		rooms = rooms_i

	new_element = (rooms, start_time, end)
	B.append(new_element)
	print(B)

	print(end_i)
	print(end_j)
	if end_i < end_j:
		print('passou aqui')
		start_time = start_i
		end = end_i
		rooms = rooms_i + rooms_j
		i += 1
	
	elif end_i > end_j:
		start_time = start_i
		end = end_j
		rooms = rooms_i + rooms_j
		j += 1

	new_element = (rooms, start_time, end)
	B.append(new_element)
	print(B)
	breakpoint()

