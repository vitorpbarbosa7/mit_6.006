


B = (1,3,4)

def _move_tuple(B, marker):
	
	if marker == B[i][1]:
		# update market because it is still possible
		marker = B[i][2]
	else:
		#moving marker inside tuple is not possible anymore, so move it to next element
		i+=1
		marker = B[i][1]

