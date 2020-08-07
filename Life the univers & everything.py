while True:
	try:		
		n = int(input())
		if n != 42:
			print(n)
		else:
			break
			
	except:
		print('error')