


a = 0
n = 10000
card = 9999

k = 1
left = a
right = n
flip = False

if card > k:
	previous_direction = 'n'
else:
	previous_direction = 's'

counter = 0
while k != card:
	breakpoint()
	if card > k:
		print('north')
		direction = 'n'
		
		if not flip:
			k = k + 2**counter
			counter += 1
		else:
			left = k
			k = (left + right)//2
			#left = k
			#k = (left + right)//2
		print(f'new k: {k} \n')
	
		if direction != previous_direction:
			flip = True

		previous_direction = direction
			
	else:
		print('south')

		direction = 's'
		if not flip:
			k = k - 2**counter
			counter += 1
		else:
			right = k
			k = (left + right)//2
			#right = k
			#k = (left + right)//2
		print(f'new k: {k} \n')
		
		if direction != previous_direction:
			flip = True

		previous_direction = direction
