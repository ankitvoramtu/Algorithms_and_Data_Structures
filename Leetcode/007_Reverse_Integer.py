def reverse(x):
	ret = 0
	INT_MAX = 2147483647
	INT_MIN = -2147483648

	if x == INT_MIN:  # Process special number first, ** KEY step
		return 0
	
	original_x = x
	while x != 0:
		# Extreme case: out of boundary
		if ret > (INT_MAX - abs(x) % 10) / 10.0:  # ** KEY step
			return 0
		else:
			ret = ret * 10 + abs(x) % 10
		x = abs(x) // 10
	  #Two cases
	if original_x > 0:
		return ret
	else:
		return ret * (-1)
	
