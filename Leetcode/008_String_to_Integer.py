def myAtoi(str):
	sign = 1
	i = 0
	INT_MAX = 2147483647
	INT_MIN = -2147483648
	ret  = 0

	  # Remove space
	while i < len(str):
		if str[i] == ' ':
			i = i + 1
		else:
			break

	if i < len(str) and str[i] == '+':
	 	i = i + 1
	elif i < len(str) and str[i] == '-':
		i = i + 1
		sign = -1

	while i < len(str):
		if str[i] in '0123456789':
			num = ord(str[i]) - ord('0')
			if sign == 1 and ret > (INT_MAX - num) * 1/ 10:  # (ret * 10 + num) > INT_MAX
				return INT_MAX
			elif sign ==  -1 and ret > (INT_MIN + num) / (-10):  # (-ret * 10 - num) < INT_MIN
				return INT_MIN
			ret = ret * 10 + num
			i  = i + 1
		else:  #might have space in the end
			return ret * sign
	return ret * sign