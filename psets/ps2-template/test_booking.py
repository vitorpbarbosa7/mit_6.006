


B1 = [(2,2,3)]
B2 = [(1,0,4)]


cont = 0

i = 0
j = 0

rooms_i = B1[i][0]
rooms_j = B2[j][0]


start_i = B1[i][1]
start_j = B2[j][1]

end_i = B1[i][2]
end_j = B1[j][2]


if start_j < start_i:
	start_time = start_j
	end = start_i
	rooms = rooms_j
else:
	start_time = start_i
	end = start_j
	rooms = rooms_i

new_element = (rooms, start_time, end)


print(new_element)

